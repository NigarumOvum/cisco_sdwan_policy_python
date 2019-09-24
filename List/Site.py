import json

from BaseObject import BaseObject


class Site(BaseObject):

    def __init__(self,name,site_list,id=None,reference=None):
        self.type = "siteList"
        self.id = id
        self.name = name
        self.references = reference
        self._entries = site_list
        self.url= "template/policy/list/site"
        super().__init__()

    def get_entries(self):
        return self._entries

    def set_entries(self, entries):
        self.modified = True
        self._entries = entries

    @classmethod
    def from_json(cls,config):
        id = config["listId"]
        name = config["name"]
        references = config["references"]
        entries = [i["siteId"] for i in config["entries"]]

        return cls(name,entries,id,references)


    def to_json(self):
        # {"name": "DX", "description": "Desc Not Required", "type": "site", "listId": null,
        #  "entries": [{"siteId": "100"}, {"siteId": "200"}, {"siteId": "300"}]}
        return {
            "name":self.name,
            "description":"Desc Not Required",
            "type":"site",
            "listId":None,
            "entries":[
                {"siteId":i} for i in self._entries]
        }
