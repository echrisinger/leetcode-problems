class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alphanumeric_regex = re.compile('^[a-z]')
        numeric_regex = re.compile('^[0-9]')
        lettered_logs = sorted([
            log
            for log in logs
            if alphanumeric_regex.match(log.split(' ')[1])
        ], key=lambda s: (' '.join(s.split(' ')[1:]), s.split(' ')[0]))
        digit_logs = [
            log
            for log in logs
            if numeric_regex.match(log.split(' ')[1])
        ]
        return lettered_logs + digit_logs

