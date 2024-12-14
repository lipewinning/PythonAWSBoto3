

def main():

    instance_type = 't2.micro'
    message = "My instances are of type: "

    num_of_instances = 5
    hours_running = 10

    print(f"{message} {instance_type}. I have {num_of_instances} of them and they have been running {hours_running} hours.")

    instances_running = True
    print(f"Are my instances running? {instances_running}")

    instances_cost_per_hour = 0.25
    print(f"The price of running them per instance hours is {instances_cost_per_hour}")





if __name__ == '__main__':
    main()