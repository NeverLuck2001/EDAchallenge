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

### 1.2 lib - Memory Model Library Files Saved

The memory's BIST model library file may have suffixes such as .lib, .masis, .lvlib, or .memlib. Each type of memory corresponds to a memory BIST model description file. While the file formats may vary depending on the suffix, they all contain important logical function information about the memory, including but not limited to test algorithms, port types, and valid signal values.

### 1.3 lvlib - Memory DFT Model Library Files Saved

A kind of memory model library file but is specific to DFT flow.

### 1.4 verilog - Memory Verilog Files Saved

The memory's Verilog description file is in *.v file format, written in Verilog language. And each type of memory corresponds to a memory Verilog description file.

### 1.5 memorylist.f File

A text file with the suffix .f or .list. In this file, all the memories included in the design are listed, separated by memory type. Each memory is listed on a separate line, which including its complete hierarchical name.

### 1.6 layout.def File

The memory backend layout file is an excerpt from the physical design DEF (design exchange format) file, listing the physical positions of all memory cells on the layout. The file is in DEF file format, with each line containing the instance name, module name, and coordinates of the memory cell.

### 1.7 clk.txt File

The `clk.txt` file is a text file that contains the clock information for the design. It includes details such as the clock source. This file is crucial for timing analysis and synthesis processes in the design flow. Each line in the file represents a unique intence of the memory and the next line is the clock domain of itself in the design.
