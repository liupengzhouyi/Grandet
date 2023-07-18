#/bin/bash python3



class FilterRules:
    
    
    def __init__(self):
        
        self.name = ""
        self.operation = ""
        self.value = ""
    
    
    def init(self, name: str=None, operation: str="包含",value: str=None) -> None:
        
        self.name = name
        self.operation = "包含"
        self.value = value
        
        
    def init_by_json(self, info: dict) -> None:
        
        self.name = info.get("name")
        self.operation = info.get("operation")
        self.value = info.get("value")
        
    
    def __str__(self) -> str:
        
        return self.name + " " + self.operation + " " + self.value
    
        
def FilterRulesFactory(name: str=None, operation: str="包含", value: str=None) -> FilterRules:
    
    rule = FilterRules()
    rule.init(name, operation, value)
    return rule


def FilterRulesFactory_by_json(info: dict) -> FilterRules:
    
    rule = FilterRules()
    rule.init_by_json(info)
    return rule
    