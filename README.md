# TCP IP Attack
The project utilizes the TCP/IP Attack Lab provided by SEEDLAB 2.0 as a foundational platform for hands-on exploration and experimentation in the domain of network security. This lab offers practical experience in understanding and executing various TCP attacks, crucial components of contemporary cybersecurity education.

In this lab, the focus is on delving into the intricacies of TCP vulnerabilities across different attack vectors. The primary goal is to provide the skills to identify, exploit, and mitigate TCP vulnerabilities effectively.

Moreover, the lab extends to the exploration of countermeasures aimed at mitigating TCP vulnerabilities. Practical experimentation with techniques such as SYN cookies, TCP reset attacks, and reverse shells provides firsthand experience in defending against TCP-based exploits.

## Report
The detailed project report, including the methodology, findings, and analysis of TCP attack techniques and countermeasures, can be accessed in the attached `Report.pdf`.

## Additional

### Original Lab Instructions
The original lab instructions outlining the objectives, tasks, and guidelines for the TCP/IP Attack Lab can be accessed [here](https://seedsecuritylabs.org/Labs_20.04/Networking/TCP_Attacks/).

### Modified Files
The modified files according to lab instructions are as follows:
- `synflood.py`
- `synReverse.py`
- `synRST.py`
- `synSession.py`
  
The original (non-modified) files can be found in the `Labsetup` directory within this repository.

## File Structure and Content
```
tcp-ip-attack/
├── Labsetup/
│   ├── docker-compose.yml
│   └── volumes/
│       ├── synflood.c
│       ├── synFlood.py
│       ├── synReverse.py
│       ├── synRST.py
│       └── synSession.py
├── README.md
├── Report.pdf
├── synflood.py
├── synReverse.py
├── synRST.py
└── synSession.py
```
