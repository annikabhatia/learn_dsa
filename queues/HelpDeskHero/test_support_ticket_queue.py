queue = SupportTicketQueue()

queue.submit_ticket("Cannot log in to account.")
queue.submit_ticket("Website is down.")
queue.submit_ticket("Reset password issue.")

print(queue.peek_ticket())    # Output: Cannot log in to account.
print(queue.process_ticket()) # Output: Cannot log in to account.
print(queue.process_ticket()) # Output: Website is down.
print(queue.is_empty())       # Output: False
print(queue.process_ticket()) # Output: Reset password issue.
print(queue.is_empty())       # Output: True