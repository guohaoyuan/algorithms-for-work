from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import os


def txt2list(txtname):
    annotations = []
    for line in open(txtname, "r"):
        annotation = line.replace('\n', '').strip().split(' ')
        annotations.append(annotation)
    return annotations

def make_xml(annotations, filename, outputPath):

    node_root = Element('annotation')


    node_source = SubElement(node_root, 'source')
    node_filename = SubElement(node_source, 'filename')
    node_filename.text = filename.replace('.xml', '.tiff')

    node_origin = SubElement(node_source, 'origin')
    node_origin.text = 'GF2/GF3'

    node_research = SubElement(node_root, 'research')
    node_version = SubElement(node_research, 'version')
    node_version.text = '4.0'

    node_provider = SubElement(node_research, 'provider')
    node_provider.text = 'xidian'

    node_author = SubElement(node_research, 'author')
    node_author.text = 'Sailng'

    node_pluginname = SubElement(node_research, 'pluginname')
    node_pluginname.text = 'Detection'

    node_time = SubElement(node_research, 'time')
    node_time.text = '2020-07-2020-11'

    if len(annotations) > 0:
        node_objects = SubElement(node_root, 'objects')

        num_object = len(annotations)

        for annotation in annotations:
            node_object = SubElement(node_objects, 'object')
            node_coordinate = SubElement(node_object, 'coordinate')
            node_coordinate.text = 'pixel'

            node_type = SubElement(node_object, 'type')
            node_type.text = 'rectangle'

            node_description = SubElement(node_object, 'description')
            node_description.text = 'None'

            node_possibleresult = SubElement(node_object, 'possibleresult')
            node_name = SubElement(node_possibleresult, 'name')
            node_name.text = 'ship'
    ###############################################################  要改的地方
            node_probability = SubElement(node_possibleresult, 'probability')
            # node_probability.text = '1'
            node_probability.text = annotation[4]

            node_points = SubElement(node_object, 'points')



            node_point = SubElement(node_points, 'point')
            node_point.text = annotation[0] + ', ' + annotation[1]
            node_point = SubElement(node_points, 'point')
            node_point.text = annotation[0] + ', ' + annotation[3]
            node_point = SubElement(node_points, 'point')
            node_point.text = annotation[2] + ', ' + annotation[3]
            node_point = SubElement(node_points, 'point')
            node_point.text = annotation[2] + ', ' + annotation[1]
            node_point = SubElement(node_points, 'point')
            node_point.text = annotation[0] + ', ' + annotation[1]
    ####################################################################

    xml = tostring(node_root, pretty_print = False)
    dom = parseString(xml)
    save_xml = os.path.join(outputPath, filename)
    with open(save_xml, 'w') as f:
        dom.writexml(f, newl = '\n', addindent = '\t', encoding='utf-8')
    return

inputPath = '/home/ghy/GHY/CenterNet-1-bs/output_txt (另一个复件)' #txt文件夹路径
outputPath = "/home/ghy/GHY/CenterNet-1-bs/output_xml"   #xml文件夹路径
txts = os.listdir(inputPath)   #txt文件名

txtsPath = [os.path.join(inputPath, i) for i in txts]
# print(txtsPath)
for txtPath in txtsPath:
    annotations = txt2list(txtPath)
    filename = txtPath.split('/')[-1].replace('.txt', '.xml')
    make_xml(annotations, filename, outputPath)