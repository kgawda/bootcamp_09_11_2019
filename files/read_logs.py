import sys

def main():
    user_total_time_count = {} # ilość sekund spędzonych w systemie
    user_login_time = {} # moment ostatniego zalogowania się
    with open(sys.argv[1], encoding='utf-8') as f:
        for line in f:
            username, action, timestamp = line.strip().split(';')
            timestamp = int(timestamp)
            if action == 'LOGIN':
                user_login_time[username] = timestamp
            elif action == 'LOGOUT':
                time_in_this_session = timestamp - user_login_time[username]
                if username in user_total_time_count:
                    user_total_time_count[username] += time_in_this_session
                else:
                    user_total_time_count[username] = time_in_this_session

        for user, time in user_total_time_count.items():
            print(f"User {user} spent {time}s in system")

if __name__ == "__main__":
    main()