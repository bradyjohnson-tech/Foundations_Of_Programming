import Personnel

# Initializing Personnel objects
doctor = Personnel.Doctor("Internal Medicine", "Dr. Bob", 50)
surgeon = Personnel.Surgeon("True", "Surgeon Dan", 45)
nurse = Personnel.Nurse(100, "Nurse Jane", 48)

# Calling the according display methods
doctor.display_doctor()
surgeon.display_surgeon()
nurse.display_nurse()
