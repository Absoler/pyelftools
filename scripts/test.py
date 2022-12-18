#! /usr/bin/python3
import sys
sys.path.insert(0, '.')
from elftools.elf.elffile import ELFFile

from iced_x86 import *

def create_enum_dict(module):
    ''' for descript iced_x86 int attributes
    '''
    return {module.__dict__[key]:key for key in module.__dict__ if isinstance(module.__dict__[key], int)}

# with open("/home/patcher/binaryPatterns/ifRefresh/1667_gcc-12.1_output.o", "rb") as f:
#     elf = ELFFile(f, sys.stdout)
#     text = elf.get_section_by_name('.text')
#     textInfo = text.stream.read()
#     print(len(textInfo))
#     addr = text['sh_addr']
#     code = text.data()
#     # print(code)
#     opKindDict = create_enum_dict(OpKind)
#     codeDict = create_enum_dict(Code)
#     regDict = create_enum_dict(Register)
#     decoder = Decoder(64, code, 0)
#     for ins in decoder:
#         print(f'{ins.ip:X} {ins} {opKindDict[ins.op0_kind]}')
#         if "BRANCH" in opKindDict[ins.op0_kind]:
#             kind = opKindDict[ins.op0_kind].lower()
#             val = getattr(ins, kind)
#             print(f"    {val:X}")
#         if "MOV" in codeDict[ins.code] and "MEMORY" in opKindDict[ins.op1_kind]:
#             print(f"   base:{regDict[ins.memory_base]}   index:{regDict[ins.memory_index]}")

codeDict = create_enum_dict(OpKind)
# for key in codeDict:
#     print(f'{key:X} {codeDict[key]}')
for item in dir(Instruction):
    print(item)