# Introduction for GWX Testcases

---

## 1. Directories Structure

edac_gwx_testcases
├── testcase01
│&emsp;&emsp;├── ds
│&emsp;&emsp;├── lib
│&emsp;&emsp;├── lvlib
│&emsp;&emsp;└── verilog
└── testcase03
&emsp;&emsp;&emsp;&emsp;├── ds
&emsp;&emsp;&emsp;&emsp;├── lib
&emsp;&emsp;&emsp;&emsp;├── lvlib
&emsp;&emsp;&emsp;&emsp;└── verilog
&emsp;&emsp;&emsp;&emsp;memorylist.f
&emsp;&emsp;&emsp;&emsp;design.spec
&emsp;&emsp;&emsp;&emsp;clock.sdc
&emsp;&emsp;&emsp;&emsp;layout.def
&emsp;&emsp;&emsp;&emsp;clk.txt
...
tc.log
readme.md

### 1.1 ds - Memory Datasheet Files Saved

A text file with the suffix .ds. This file serves as the datasheet for the memories, with each memory corresponding to a data table within the file. It contains essential information about the memories, such as area and power consumption.

后缀为 .ds 的文本文件。该文件是存储器的数据表，每个存储器对应文件中的一个数据表。它包含存储器的基本信息，如面积和功耗。
### 1.2 lib - Memory Model Library Files Saved

The memory's BIST model library file may have suffixes such as .lib, .masis, .lvlib, or .memlib. Each type of memory corresponds to a memory BIST model description file. While the file formats may vary depending on the suffix, they all contain important logical function information about the memory, including but not limited to test algorithms, port types, and valid signal values.

内存 BIST 模型库文件的后缀可能是 .lib、.masis、.lvlib 或 .memlib。每种类型的内存都对应一个内存 BIST 模型描述文件。虽然文件格式可能因后缀而异，但它们都包含有关存储器的重要逻辑功能信息，包括但不限于测试算法、端口类型和有效信号值。
### 1.3 lvlib - Memory DFT Model Library Files Saved

A kind of memory model library file but is specific to DFT flow.

一种内存模型库文件，但专门用于 DFT 流程。
### 1.4 verilog - Memory Verilog Files Saved

The memory's Verilog description file is in *.v file format, written in Verilog language. And each type of memory corresponds to a memory Verilog description file.

存储器的 Verilog 描述文件采用 *.v 文件格式，用 Verilog 语言编写。每种类型的存储器都对应一个存储器 Verilog 描述文件。
### 1.5 memorylist.f File

A text file with the suffix .f or .list. In this file, all the memories included in the design are listed, separated by memory type. Each memory is listed on a separate line, which including its complete hierarchical name.

后缀为 .f 或 .list 的文本文件。在该文件中，设计中包含的所有存储器都按存储器类型列出。每个存储器都单独列出一行，包括其完整的层次名称。
### 1.6 layout.def File

The memory backend layout file is an excerpt from the physical design DEF (design exchange format) file, listing the physical positions of all memory cells on the layout. The file is in DEF file format, with each line containing the instance name, module name, and coordinates of the memory cell.

内存后台布局文件是物理设计 DEF（设计交换格式）文件的摘录，列出了布局上所有内存单元的物理位置。该文件采用 DEF 文件格式，每行包含内存单元的实例名称、模块名称和坐标。
### 1.7 clk.txt File

The `clk.txt` file is a text file that contains the clock information for the design. It includes details such as the clock source. This file is crucial for timing analysis and synthesis processes in the design flow. Each line in the file represents a unique intence of the memory and the next line is the clock domain of itself in the design.

clk.txt 文件是一个文本文件，其中包含设计的时钟信息。它包括时钟源等详细信息。该文件对于设计流程中的时序分析和综合过程至关重要。文件中的每一行都代表存储器的一个唯一值，下一行是设计中自身的时钟域。