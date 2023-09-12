import json
import xml.etree.ElementTree as etree


class JSONConnector:
    def __init__(self, filepath):
        """
        解析json文件的工厂
        """
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        """
        解析XML文件的工厂
        """
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith("json"):
        connector = JSONConnector
    elif filepath.endswith("xml"):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to("data/person.sq3")  # Cannot connect to data/person.sq3
    print()

    xml_factory = connect_to("data/person.xml")
    xml_data = xml_factory.parsed_data
    parse_str = ".//{}[{}='{}']".format("person", "firstName", "SteveRocket")
    liars = xml_data.findall(parse_str)
    print("found: {} persons".format(len(liars)))
    for liar in liars:
        print("first name: {}".format(liar.find("firstName").text))
        print("last name: {}".format(liar.find("lastName").text))
        [
            print("phone number ({})".format(p.attrib["type"]), p.text)
            for p in liar.find("phoneNumbers")
        ]
    print()

    json_factory = connect_to("data/donut.json")
    json_data = json_factory.parsed_data
    print("found: {} donuts".format(len(json_data)))
    for donut in json_data:
        print("name: {}".format(donut["name"]))
        [print("topping: {} {}".format(t["id"], t["type"])) for t in donut["topping"]]


if __name__ == "__main__":
    main()
