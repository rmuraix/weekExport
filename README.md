# WeekExport
[![Build](https://github.com/rmuraix/weekExport/actions/workflows/build.yml/badge.svg)](https://github.com/rmuraix/weekExport/actions/workflows/build.yml)
[![DeepSource](https://deepsource.io/gh/rmuraix/weekExport.svg/?label=active+issues&token=UgBDSqrPFnTHj9hfza8F_ora)](https://deepsource.io/gh/rmuraix/weekExport/?ref=repository-badge)
[![codecov](https://codecov.io/gh/rmuraix/weekExport/branch/main/graph/badge.svg?token=9NAC1P80DY)](https://codecov.io/gh/rmuraix/weekExport)  
## About
Outputs dates to the clipboard.  
## Requirements
Linux: xclip or xsel commands and gtk or PyQt4 modules.  
## Usage
- Download latest release in [here](https://github.com/rmuraix/weekExport/releases).  
### Configuration Options
You can set it up by placing a file `./run_config.json`  
If it does not exist, it will be generated automatically.  

**Default**  
```json
{
    "style": "EN",
    "start": 1,
    "loop": 1,
    "days": 7
}
```  
| Key   | Type    | Value        |
| :---: | :-----: | :----------: |
| style | string  | `EN` or `JP` |
| start | integer | any          |
| loop  | integer | n > 0        |
| days  | integer | 0 < n < 8    |  

`style`: Set the language of the day  
`start`: Sets the week to start(example (`0`: this week , `1`: next week , `-1`: last week))  
`loop`: Set the number of weeks to output  
`days`: Set the number of days per week  

**Example 1**  
Execution Date: 13/08/2022  
JSON:  
```json
{
    "style": "EN",
    "start": 1,
    "loop": 2,
    "days": 4
}
```  
Output:  
> 08/15(Mon)  
> 08/16(Tue)  
> 08/17(Wed)  
> 08/18(Thu)  
> 08/22(Mon)  
> 08/23(Tue)  
> 08/24(Wed)  
> 08/25(Thu)  

**Example 2**  
Execution Date: 13/08/2022  
JSON:  
```json
{
    "style": "JP",
    "start": -1
}
```  
Output:  
> 08/01(月)  
> 08/02(火)  
> 08/03(水)  
> 08/04(木)  
> 08/05(金)  
> 08/06(土)  
> 08/07(日)  

## Build
Windows and Linux  
```bash
nuitka --onefile src/weekexport.py
```  
Mac  
```bash
nuitka --onefile --macos-create-app-bundle src/weekexport.py
```  
## Contributing  
Please read [CONTRIBUTING.md](./.github/CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](./.github/CODE_OF_CONDUCT.md)   
## Auther
Ryota Murai ([@rmuraix](https://github.com/rmuraix))  
## License
'rmuraix/weekExport' is under [MIT License](/LICENSE).