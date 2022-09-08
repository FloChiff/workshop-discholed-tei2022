# -*- UTF-8 -*-

import argparse
from cgitb import text
import os

from bs4 import BeautifulSoup
from numpy import block
from tqdm import tqdm

def get_list_of_xml_files(path_folder):
    """List usable files from input folder"""
    abs_path_folder = os.path.abspath(path_folder)
    file_paths = []
    if os.path.isdir(abs_path_folder):
        file_paths = [os.path.join(abs_path_folder, f) for f in os.listdir(abs_path_folder)]
    else:
        print("Failed to load input. Are you sure the path to the directory is correct:\n",
        "\t", abs_path_folder)
    file_paths = [file for file in file_paths if file.endswith(".xml") and not file.endswith(".modified.xml")]
    return file_paths

def load_lines_from_txt_file(path):
    """Load content of a txt file if it exists"""
    blocks = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as fh:
            content = fh.read()
        blocks = content.split("==--==--==--==\n")
        if len(blocks) == 1:
            print("Info: there's only lines for one page in the txt file.")
        elif len(blocks) == 0:
            print("It looks like the txt file is empty.")
    fblocks = []
    for block in blocks:
        fblocks.append([line for line in block.split("\n") if len(line) > 0])
    return fblocks 

def load_xml_from_alto_file(path):
    """Load content of a file if it exists"""
    soup = False
    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as fh:
            content = fh.read()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception as e:
            print("Error, could not parse XML file")
            print(e)
    #check that it's ALTO
    if soup and not soup.alto:
        soup = False
        print("No <alto> tag in this XML. Are you sure it's a ALTO XML file?")
    elif soup:
        alto4_namespaces = set(["http://www.loc.gov/standards/alto/ns-v4#"])
        if not alto4_namespaces.intersection(soup.alto.attrs.get("xmlns", "").split(" ")) == alto4_namespaces:
            print("Failed to match expected namespace declaration.", 
            "Are you sure this is an ALTO 4.2 file?")
            print(soup.alto.attrs.get("xmlns", "").split(" "))
            soup = False
    if soup is False:
        print("Soup is False... ")
    return soup

def order_xml_files(files):
    """Return correctly ordered file paths (1,2,10,21 in stead of 1,10,2,21)"""
    # assuming they were imported as PDF in eScriptorium
    # so they look like filename_1.xml, filename_2.xml, ...
    new_files = []
    bases = []
    nums = []
    for file in files: 
        base, n = file.split("PP3_p")
        bases.append(base)
        nums.append(n)
    if len(set(bases)) < 1:
        print("There's more than 1 basename for the XML file, maybe you should do",
            "several runs.")
    else:
        nums = [int(n.replace(".xml", "")) for n in nums]
        nums.sort()
        new_files = [f'{"PP3_p".join([b, str(n)])}.xml' for b,n in zip(bases, nums)]
    return new_files

def save_new_xml_file(soup, path):
    new_path = path.replace(".xml", ".modified.xml")
    with open(new_path, "w+", encoding="utf8") as fh:
        fh.write(str(soup))

def main(path_to_xml_files, path_to_txt_file):
    xml_files = order_xml_files(get_list_of_xml_files(path_to_xml_files))
    txt_blocks = load_lines_from_txt_file(path_to_txt_file)

    if len(txt_blocks) != len(xml_files):
        print("Too many or too little text blocks compared for the XML files. (XML files: ", len(xml_files),
        "; TXT blocks: ", len(txt_blocks), ")", sep="")
    else:
        for alto_file, text_block in tqdm(zip(xml_files, txt_blocks), total=len(xml_files)):
            xml_tree = load_xml_from_alto_file(alto_file)
            textlines = xml_tree.find_all("TextLine")
            if xml_tree:
                if len(text_block) != len(textlines):
                    print("\nToo many or too little lines in text block compared to the number of Text Line. (TextLine: ",
                    len(textlines), "; Txt block: ", len(text_block), sep="")
                    print("In file:", alto_file, "\n")
                else:
                    for textline, newline in zip(textlines, text_block):
                        content = textline.String.attrs.get("CONTENT", False)
                        if content is False:
                            print("TextLine with ID", textline.attrs.get("ID"), "has a CONTENT-less String child.")
                        else:
                            textline.String.attrs["CONTENT"] = newline
                    save_new_xml_file(xml_tree, alto_file)


parser = argparse.ArgumentParser()
#parser.add_argument("--test", help="execute on test files", action="store_true")
parser.add_argument("-x", "--xml", nargs=1, help="path to folder containing xml files")
parser.add_argument("-t", "--txt", nargs=1, help="path to source txt file")
args = parser.parse_args()

main(args.xml[0], args.txt[0])



# TODO : 
# - order xml file before the loop!