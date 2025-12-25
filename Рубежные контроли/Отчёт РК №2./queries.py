def find_procedures_ending_with_ov(procedures, databases):
    return [
        (sp.name, next(db.name for db in databases if db.id == sp.db_id))
        for sp in procedures if sp.name.endswith("ов")
    ]

def average_salary_by_database(procedures, databases):
    result = []
    for db in databases:
        db_procedures = [sp for sp in procedures if sp.db_id == db.id]
        if db_procedures:
            avg_salary = sum(len(sp.name) for sp in db_procedures) / len(db_procedures)  # пример количественного признака
            result.append((db.name, avg_salary))
    return sorted(result, key=lambda x: x[1])

def databases_starting_with_a(procedures, databases, sp_dbs):
    result = []
    for db in databases:
        if db.name.startswith("А"):
            db_procedures = [
                sp.name for sp in procedures if sp.db_id == db.id
            ]
            result.append((db.name, db_procedures))
    return result