from services.student_service import StudentService


def main():
    service = StudentService()

    print("=" * 55)
    print("  Student Management System - Add Student")
    print("=" * 55)

    # ---- Test 1: Valid student ----
    print("\n[TEST 1] Adding a valid student...")
    success, message = service.add_student(
        student_id="S001",
        name="Kamal Perera",
        email="kamal@example.com",
        age=20,
        course="Software Engineering",
    )
    print(f"  Result : {'OK' if success else 'FAIL'} {message}")

    # ---- Test 2: Empty email (Task 03 example) ----
    print("\n[TEST 2] Adding student with empty email...")
    success, message = service.add_student(
        student_id="S002",
        name="Nimal Silva",
        email="",
        age=22,
        course="Data Science",
    )
    print(f"  Result : {'OK' if success else 'FAIL'} {message}")

    # ---- Test 3: Duplicate ID ----
    print("\n[TEST 3] Adding student with duplicate ID...")
    success, message = service.add_student(
        student_id="S001",
        name="Amali Fernando",
        email="amali@example.com",
        age=21,
        course="Cyber Security",
    )
    print(f"  Result : {'OK' if success else 'FAIL'} {message}")

    # ---- Test 4: Invalid age ----
    print("\n[TEST 4] Adding student with invalid age (12)...")
    success, message = service.add_student(
        student_id="S003",
        name="Sahan Kumara",
        email="sahan@example.com",
        age=12,
        course="Networking",
    )
    print(f"  Result : {'OK' if success else 'FAIL'} {message}")

    # ---- Test 5: Invalid email format ----
    print("\n[TEST 5] Adding student with invalid email format...")
    success, message = service.add_student(
        student_id="S004",
        name="Dilini Jayasuriya",
        email="dilini-no-at-sign",
        age=23,
        course="AI",
    )
    print(f"  Result : {'OK' if success else 'FAIL'} {message}")

    # ---- Show all stored students ----
    print("\n" + "=" * 55)
    print("  All Stored Students")
    print("=" * 55)
    for s in service.get_all_students():
        print(f"  {s}")

    print("\nDone.")

        # ---- Search Tests ----
    print("\n" + "=" * 55)
    print("  Search Functionality Tests")
    print("=" * 55)

    # Add one more student for search testing
    service.add_student(
        student_id="S002",
        name="Nimal Silva",
        email="nimal@example.com",
        age=22,
        course="Data Science",
    )

    # Search Test 1: Valid keyword
    print("\n[SEARCH 1] Searching for 'kamal'...")
    success, results, msg = service.search_by_name("kamal")
    print(f"  Result : {msg}")
    for s in results:
        print(f"  -> {s}")

    # Search Test 2: Partial match (case-insensitive)
    print("\n[SEARCH 2] Searching for 'PERERA' (uppercase)...")
    success, results, msg = service.search_by_name("PERERA")
    print(f"  Result : {msg}")
    for s in results:
        print(f"  -> {s}")

    # Search Test 3: No match
    print("\n[SEARCH 3] Searching for 'xyz123' (no match)...")
    success, results, msg = service.search_by_name("xyz123")
    print(f"  Result : {msg}")

    # Search Test 4: Empty keyword
    print("\n[SEARCH 4] Searching for empty string...")
    success, results, msg = service.search_by_name("")
    print(f"  Result : {msg}")

    # Search Test 5: Whitespace only
    print("\n[SEARCH 5] Searching with only spaces...")
    success, results, msg = service.search_by_name("   ")
    print(f"  Result : {msg}")


if __name__ == "__main__":
    main()