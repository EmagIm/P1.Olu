import psutil, datetime, time, cProfile, re
from ProgramClass import LogisticRegML, \
    LinearRegML
from time import sleep


class ResourceMonitor:
    def __init__(self, proc_id):
        self.start_monitor = True
        self.process = proc_id
        self.program_thread = psutil.Process(pid=self.process)
        self.cpu_cores = psutil.cpu_count()

    def cpuUsage(self):
        time_stamp = time.time()
        print(datetime.datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S"))

        cpu_usage = self.program_thread.cpu_times()
        # current_cpu = self.program_thread.cpu_num()
        available_core = len(self.program_thread.cpu_affinity())
        print(f"\n# CPU cores: \n \t{self.cpu_cores}\n")
        # print(f"\n Using CPU: \n \t{current_cpu}\n")
        print(f"\nCPU available for Process: \n \t{available_core}\n")
        print(f"\n CPU use: User, System, Interrupt = \n \t {cpu_usage}\n")

    def cpuUtilization(self):
        cpu_utilization = self.program_thread.cpu_percent(interval=0.1)
        cpu_thread = self.program_thread.num_threads()
        context_switch = self.program_thread.num_ctx_switches()
        sleep(0.1)

        print(f"\n CPU utilization % : \n \t {cpu_utilization / self.cpu_cores}\n")
        print(f"\n CPU thread for Process: \n \t {cpu_thread}\n")
        print(f"\n Context Switching on Process: \n \t {context_switch}\n")

    def memoryUsage(self):
        max_memory = self.program_thread.memory_info()
        mem_map = self.program_thread.memory_maps()
        mem_percent = self.program_thread.memory_percent()

        print(f"\n Memory Analysis: \n \t {max_memory}\n")
        print(f"\n Memory Map: \n \t {mem_map}\n")
        print(f"\n Memory Percentage(RSS): \n \t {mem_percent}\n")

    def diskMemoryIO(self):
        disk_usage = self.program_thread.io_counters()

        print(f"\n Disk I/O use: \n \t {disk_usage}\n")


# def main():
#     process_1 = LogisticRegML.LogRegression_P1()
#     #process_2 = LinearRegML.LinRegression()
#     pid_1 = process_1.get_pid()
#     #pid_2 = process_2.get_pid()
#     monitor = ResourceMonitor(pid_1)
#     monitor.cpuUsage()
#     monitor.cpuUtilization()
#     monitor.memoryUsage()
#     monitor.diskMemoryIO()
#     monitor.start_monitor = False
#     print(cProfile.run('re.compile("process")'))
#
#
# if __name__ == '__main__':
#     run_time = time.time()
#     main()
#     print("%.2f sec" % (time.time() - run_time))
