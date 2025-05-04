
def format_text (text:str,prefix:str="",suffix:str="",capitalize : bool=False,max_length:int=None)->str:
   
    if not isinstance(text,str):
     raise TypeError("the input must be a string")
    if not isinstance(prefix,str):
        raise TypeError("prefix must be a string")
    if not isinstance(suffix,str):
        raise TypeError("suffix must be  a string")
    if max_length is not None:
        if not isinstance(max_length,int):
            raise TypeError("max_length must be an integer")
        if max_length<=0:
            raise ValueError("max_length must be a positive integer")
    formatted=text.strip()
    if capitalize:
        formatted=formatted.capitalize()
        formatted=f"{prefix}{formatted}{suffix}"
        if max_length is not None:
            formatted=formatted[:max_length]
        return formatted
 
ip = input("Please enter a text to format: ")
prefix = input("Enter Prefix: ")
suffix = input("Enter suffix: ")
print(format_text(ip))
print(format_text(ip,prefix=prefix,suffix=suffix,capitalize=True))        
print(format_text("sampletext",max_length=8))