### Comprehensive Guide: Python Data Structures in Hospital Management 🏥🐍

```markdown
Python Data Structures for Hospital Management Systems

This guide explores Python data structures through hospital management analogies, making complex concepts intuitive and practical. All code uses **Python 3.13** with zero external dependencies.

---

### Key Workflows
1. **Patient Admission**: `admit_patient("John Doe", "Fracture", priority=True)`  
2. **ER Processing**: `next_patient = er_queue.popleft()`  
3. **Medication Dispensing**: `med = medication_stack.pop()`  
4. **Doctor Login**: `verify_password(stored_hash, salt, attempt)`  
5. **Equipment Sterilization**: `sterile_tools -= contaminated_tools`

---

## 🏃 Running the System

1. Clone the repository:
```bash
git clone https://github.com/chankjen/Python_Data_Structures.git
cd hospital-ds
```

2. Run the demo simulation:
```bash
python hospital_system.py
```

3. Sample test credentials:
```
Username: dr_grey
Password: SeattleGrace1!  # Pre-registered in demo
```

---

## 🔒 Security Best Practices

1. **Password Storage**
   - Always use PBKDF2, bcrypt or scrypt
   - Never store plaintext passwords
   - Minimum 100,000 iterations for PBKDF2

2. **Data Protection**
   ```python
   # Sensitive data handling
   from cryptography.fernet import Fernet
   
   key = Fernet.generate_key()
   cipher = Fernet(key)
   encrypted_data = cipher.encrypt(b"Sensitive patient info")
   ```

3. **Access Control**
   - Implement role-based access control (RBAC)
   - Use decorators for permission checks:
   ```python
   def requires_access(permission):
       def decorator(func):
           def wrapper(*args, **kwargs):
               if permission not in current_user.access:
                   raise PermissionError("Access denied")
               return func(*args, **kwargs)
           return wrapper
       return decorator
   
   @requires_access("patient_records")
   def view_medical_history(patient_id):
       # ... function logic
   ```

---

## Data Structure Selection Guide
| Scenario | Recommended Structure | Hospital Use Case |
|----------|------------------------|-------------------|
| First-In-First-Out | `deque` | Patient triage |
| Last-In-First-Out | `list` as stack | Medication dispensing |
| Key-Value Lookups | `dict` | Patient records |
| Unique Items | `set` | Sterile equipment |
| Immutable Data | `tuple` | Hospital coordinates |
| Ordered Collection | `list` | Ward bed assignments |

---
> "Good data structures are like well-organized hospital wards - they save lives (and runtime)!" 🐍💉
```
