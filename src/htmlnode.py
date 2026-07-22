class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_str}"
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        if self.children or other.children:
            if len(self.children) != len(other.children):
                return False
            for child_self, child_other in zip(self.children, other.children):
                if child_self != child_other:
                    return False
        if self.props or other.props:
            if len(self.props) != len(other.props):
                return False
            for key in self.props:
                if other.props.get(key) != self.props.get(key):
                    return False
        return (self.tag == other.tag and
                self.value == other.value)
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"