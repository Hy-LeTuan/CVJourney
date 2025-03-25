# Virtual Machines

Before learning what Docker is and why we need Docker, we have to learn about its predecessor, the Virtual Machine which works through a process called virtualization.

Virtualization is a technology where you can simulate multiple different devices running different operating system right on your current device. A device that you are simulating is called a guest and your current device is called the host. When you create a Virtual Machine, you allocate a part of your resources (CPU power, RAM) to the guest machine and the host and guest communicates and shares information through a hypervisor (a piece of software that manages virtual machines).

**The advantage** of virtual machine is that it allows users to run multiple operating systems on the same machine, where these operating systems can use different kernels (the code for the operations of the operating system). This means you can run Windows and Linux on a MacBook without any problem.

**The disadvantage** of virtual machine is that since all guest machines communicate through the hypervisor, this makes resource sharing and information exchange between the host and the guests slow, reducing the performance of the guest machines

# Docker vs. Virtual Machine

Docker is similar to Virtual Machines in the sense that it also allows you to simulate multiple operating systems on your host device. The only difference between Docker and VMs that you need to care about is that Docker does not use a hypervisor. Instead, guest machines directly interact with the host resources and will take as much resource as needed. This means that Docker is **faster** than VMs, but it also means that the **kernel between the guest and the host have to be the same**. This means that you cannot simulate a Linux machine on your Windows device using Docker _without taking more actions_, but you can run any Linux operating system if you are currently using a Linux device.

# Docker fundamentals

## How Docker actually works

The main technology powering Docker is called **containerization**. The containerization process takes a piece of software and package it into a single or multiple containers. A container contains everything the software needs to run. This includes: the operating system, the operating system packages and the software's dependencies.

Docker helps you create and manage these containers efficiently by automating the containerization process for you, the only thing you need to do is to specify what needs to be included in the container. You store the requirements and the commands of creating a container, including which operating system to use, which packages to install and other commands that has to be executed in a **Docker Image**, which is just a normal text file that that contains these requirements.

After writing your Docker Image, you can use this image to generate **as many containers as you want**. You can then manage these containers independently of each other, and any changes made on a container DOES NOT affect other containers.

# Running Docker on Windows and MacBook

As stated earlier, Docker containers requires the host OS to use the same kernel as them, so that they can share resources without having to communicate through a hypervisor, which is why you cannot run a Linux container on a MacBook or a Windows machine. To fight this problem, MacBook and Windows each offer their own solution to allow users to run Docker.

**On Windows**, Microsoft allows us to install **Windows Subsystem for Linux**, which is essentially a way for us to install the Linux kernel right on Windows. With WSL installed, we can easily use this kernel to run any Linux Docker container we want.

**On MacBook**, Apple does not allow us to install a Linux kernel like on Windows, but Docker offers a solution where the **Docker Desktop App** for MacBook contains a very lightweight Virtual Machine that is equipped with a Linux kernel, allowing you to run Docker container using the Linux kernel of this virtual machine. The upside of this method is that Docker's VM is very ligthweight and is not a fully fledged Virutal Machine, so it keeps your MacBook light and fast.
