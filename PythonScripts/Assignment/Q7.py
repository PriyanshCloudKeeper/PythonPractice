# Q7. EC2 Recommendation
# Python script that provides EC2 instance recommendations based on a given instance's type, size, and CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing performance and costs based on the utilization metrics.
# Input:
# Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano, t3.medium).
# CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).

# The output will be a recommendation for a new EC2 instance based on the following logic:

# Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.
# Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size but suggest the latest generation instance type.
# Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.
 
# Instance Size Comparison: The EC2 instance sizes follow a specific hierarchy:

# nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge > 16xlarge > 32xlarge..

# If the CPU is underutilized (CPU < 20%), the script should recommend a smaller instance by one step.
# If the CPU is overutilized (CPU > 80%), the script should recommend a larger instance by one step.
# If the instance size is the smallest (nano), it cannot be reduced further, so no smaller size is recommended.
# If the instance is the largest (32xlarge), it cannot be upgraded further.

# Input 1: 
# Current EC2 : t2.large
# CPU : 20%

# Output 1:
# Table showing columns and its value (use Que 6 function to make table with following columns)
# Columns are : serial no., current ec2, current CPU, status, recommended ec2

# Optional: use boto3 to get the CPU metric using cloudwatch cliet get_metric_data


# import re
# instance_sizes = "nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge > 16xlarge > 32xlarge"
# instance_sizes = re.sub(r"\s+", "", instance_sizes, flags=re.UNICODE)
# instance_sizes = "nano>micro>small>medium>large>xlarge>2xlarge>4xlarge>8xlarge>16xlarge>32xlarge".split(">")


def utilization_check(cpu, index):

    # Underutilized
    if cpu < 20:
        index = index - 1
    # Overutilized
    elif cpu > 80:
        index = index + 1
    # Average Utilization
    elif 20 < cpu < 80:
        index = index

    return index

ec_type = input("Current EC2: ")
cpu = input("CPU: ")
if type(cpu) == str:
    cpu = int(cpu.split('%')[0])

instance_sizes = ['nano', 'micro', 'small', 'medium', 'large', 'xlarge', '2xlarge', '4xlarge', '8xlarge', '16xlarge', '32xlarge']

size = ec_type.split(".")[1]
if size in instance_sizes:
    
    index = instance_sizes.index(size)
    
    # if first
    if index == 0:
        print("Instance size is the smallest (nano), it cannot be reduced further, so no smaller size is recommended but the instance type can be upgraded to latest generation.")

    # if last
    elif index == (len(instance_sizes)-1):
        print("Instance is the largest (32xlarge), it cannot be upgraded further but the instance type can be upgraded to latest generation.")
    
    # in between, can recommend something
    else:
        rec_index = utilization_check(cpu, index)
        if index == rec_index:
            print("We recommend that you keep the the same instance size but the instance type can be upgraded to latest generation.")
        else:
            print(f"Your recommended instance size is: {instance_sizes[rec_index]}")

else:
    print("Please enter a correct instance type and size")
