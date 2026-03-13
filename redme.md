# 🗳️ Voting Management System using Simple Blockchain

A menu-driven console application built using **Python** that simulates a secure voting system using basic **Blockchain concepts**.

This project demonstrates how blockchain can be used to maintain **vote integrity**, prevent **double voting**, and ensure **data transparency**.

---

## 🎯 Objective

The objective of this project is to:

- Implement a simple blockchain
- Manage voters and candidates
- Record votes securely as blockchain transactions
- Validate the blockchain for data integrity

---

## 🚀 Features

✅ Add Candidates (Admin Action)  
✅ Add Voters (Admin Action)  
✅ Cast Vote (One voter → One vote)  
✅ Prevent Duplicate Voter IDs  
✅ Prevent Duplicate Candidate IDs  
✅ Prevent Double Voting  
✅ Store Votes in Blockchain Blocks  
✅ Print Full Blockchain Data  
✅ Validate Blockchain Integrity  
✅ Menu-Driven Console Interface  

---

## 🧠 Blockchain Concept Used

Each vote is stored as a **transaction inside a block**.

Each block contains:

- Block Index  
- Timestamp  
- Transaction Details (Vote Info)  
- Previous Block Hash  
- Current Block Hash  

This ensures:

🔐 Security  
🔗 Data Linking  
🛡️ Tamper Detection  

If any block data is changed, the blockchain becomes **invalid**.

---