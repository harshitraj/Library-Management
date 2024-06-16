from models import StudentExtra

duplicate_emails = StudentExtra.objects.values('email').annotate(count=models.Count('email')).filter(count__gt=1)


if duplicate_emails:
    print("Duplicate email values found:")
    for email in duplicate_emails:
        print(email['email'])
else:
    print("No duplicate email values found.")
