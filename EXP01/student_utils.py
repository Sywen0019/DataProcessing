def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(fields)}")
    name = fields[0].strip()
    if not name:
        raise ValueError("姓名不能为空")
    try:
        score = int(fields[1].strip())
    except ValueError as error:
        raise ValueError(f"成绩必须是整数：{fields[1].strip()!r}") from error
    if not 0 <= score <= 100:
        raise ValueError(f"成绩必须在 0～100 范围内：{score}")
    return {"name": name, "score": score}
