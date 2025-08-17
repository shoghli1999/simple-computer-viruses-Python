# Simple Computer Viruses - Educational Project

> **⚠️ WARNING: This project contains educational demonstrations of potentially harmful code. Use only in isolated, controlled environments for learning purposes.**

## Overview

This repository contains educational demonstrations of simple computer viruses and malicious scripts created as part of a **Network Security course** in December 2020. These examples are designed to help students understand malware behavior patterns, replication mechanisms, and the importance of cybersecurity awareness.

## 🎯 Educational Purpose

This project serves as a hands-on learning tool for:
- Understanding how viruses replicate and spread
- Analyzing different types of malicious behaviors
- Learning defensive programming techniques
- Developing cybersecurity awareness
- Studying malware behavior patterns in a controlled environment

## 📁 Project Contents

### Python Viruses

#### `s01.py` - Self-Replicating Virus
- Creates copies of itself with random names
- Executes the copied files
- Opens Google in the browser
- Demonstrates basic virus replication techniques

#### `del.py` - Destructive Script
- Deletes all files from the G: drive
- Uses Windows command line operations
- Shows destructive malware behavior

### VBScript Viruses

#### `box.vbs` - Message Box Spammer
- Creates infinite loop of message boxes
- Displays "salam" (Persian for "hello")
- Demonstrates system annoyance techniques

#### `box2.vbs` - Interactive Counter Virus
- Interactive counting virus with Persian text
- Endless loop of message boxes
- Asks user if they're tired yet
- Shows social engineering aspects

#### `voice.vbs` - Voice-Based Virus
- Continuously speaks "ha ha ha"
- Uses Windows SAPI speech synthesis
- Demonstrates audio-based system annoyance

#### `New Text Document.vbs` - Simple Message Box
- Basic message box displaying "salam"
- Simple demonstration of VBScript execution

### Documentation
- `viruses.pdf` - Educational materials about computer viruses
- `viruses.pptx` - Presentation slides on virus concepts

## ⚠️ Important Disclaimers

### **FOR EDUCATIONAL USE ONLY**
- These scripts are created **exclusively for educational purposes**
- They demonstrate potentially harmful behaviors
- **DO NOT** run on production systems or personal computers
- Use only in isolated, virtual environments

### **Safety Guidelines**
1. **Never execute on a real system**
2. Use virtual machines or sandboxed environments
3. Ensure no important data is accessible
4. Disconnect from networks when testing
5. Understand the code before running

## 🛡️ Responsible Usage

This project is intended for:
- Cybersecurity students
- Security researchers
- Educational institutions
- Controlled learning environments

**Not intended for:**
- Malicious purposes
- Production environments
- Unauthorized testing
- Harmful activities

## 📚 Learning Objectives

By studying these examples, students can learn:
- **Virus Replication**: How malware copies itself
- **System Interaction**: How scripts interact with operating systems
- **Social Engineering**: Psychological manipulation techniques
- **Defensive Programming**: How to protect against such attacks
- **Security Awareness**: Understanding threat vectors

## 🚀 Getting Started

### Prerequisites
- Virtual Machine software (VirtualBox, VMware, etc.)
- Python 3.x installed
- Windows OS (for VBScript examples)
- Isolated network environment

### Setup Instructions
1. Create a new virtual machine
2. Install Python 3.x
3. Clone this repository
4. Ensure no important data is accessible
5. Disconnect from networks

## 🔬 Safe Testing Examples

### Testing Python Viruses
```bash
# In your isolated VM
python s01.py  # Will create copies and open browser
```

### Testing VBScript Viruses
```bash
# In your isolated VM
cscript box.vbs  # Will show message boxes
```

**⚠️ Always test in virtual machines only!**

## 📊 Project Status

- ✅ Educational demonstrations complete
- ✅ Documentation provided
- ✅ Safety warnings implemented
- 🔄 Future enhancements planned

## 🔧 Technical Details

### Requirements
- Python 3.x
- Windows OS (for VBScript examples)
- Virtual machine or isolated environment

### File Types
- **Python (.py)**: Cross-platform scripting
- **VBScript (.vbs)**: Windows-specific scripting
- **Documentation**: PDF and PowerPoint presentations

## 📖 Course Context

This project was developed for:
- **Course**: Network Security
- **Program**: Bachelor's Degree
- **Date**: December 2020
- **Purpose**: Hands-on malware analysis and cybersecurity education

## 🤝 Contributing

This is an educational project. If you have suggestions for:
- Additional educational examples
- Improved documentation
- Better safety warnings
- Enhanced learning materials

Please feel free to contribute through issues or pull requests.

## 📄 License

This project is for educational purposes only. Please use responsibly and in accordance with your institution's guidelines.

## 🔗 Related Resources

- [Cybersecurity Best Practices](https://www.cisa.gov/cybersecurity)
- [Malware Analysis Tools](https://www.malwarebytes.com/)
- [Virtual Machine Software](https://www.virtualbox.org/)

---

**Remember: Knowledge is power, but with great power comes great responsibility. Use this knowledge to protect, not to harm.**

*Created for educational purposes in Network Security course - December 2020*

