def count_errors(logs):
    count = 0
    for line in logs:
        if "ERROR" in line:
            count += 1
    return count

# Test
logs = [
    "INFO User logged in",
    "ERROR Database failed",
    "INFO Request processed",
    "ERROR Timeout"
]

print(count_errors(logs))


################output################
#Run started
#Initializing environment
#Installing packages
#Running code
#2

#Run completed in 4543.39999999851ms
