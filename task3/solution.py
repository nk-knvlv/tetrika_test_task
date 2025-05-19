def appearance(intervals: dict[str, list[int]]) -> int:
    total_time = 0
    for sec in range(intervals['lesson'][0] + 1, intervals['lesson'][1] + 1):
        if is_user_online(intervals['pupil'], sec) and is_user_online(intervals['tutor'], sec):
            total_time += 1
    return total_time


def is_user_online(intervals: list[int], sec: int) -> bool:
    for i in range(0, len(intervals), 2):
        if intervals[i] < sec <= intervals[i + 1]:
            return True
    return False