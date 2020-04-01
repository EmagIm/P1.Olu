import time
from concurrent.futures import ThreadPoolExecutor
from ProgramClass import LinearRegML, \
    LogisticRegML, \
    ProcessResource


def main():
    with ThreadPoolExecutor() as executor:

        try:
            program_1 = LogisticRegML.LogRegression_P1()
            program_2 = LinearRegML.LinRegression()
            executor.submit(program_1)
            executor.submit(program_2)
            PID_1 = program_1.get_pid()
            PID_2 = program_2.get_pid()

            resource_monitor = ProcessResource.ResourceMonitor(PID_1)
            executor.submit(resource_monitor.cpuUsage)
            executor.submit(resource_monitor.cpuUtilization)
            executor.submit(resource_monitor.memoryUsage)
            executor.submit(resource_monitor.diskMemoryIO)

            resource_monitor = ProcessResource.ResourceMonitor(PID_2)
            executor.submit(resource_monitor.cpuUsage)
            executor.submit(resource_monitor.cpuUtilization)
            executor.submit(resource_monitor.memoryUsage)
            executor.submit(resource_monitor.diskMemoryIO)
        finally:
            resource_monitor.start_monitor = False


if __name__ == '__main__':
    main()
