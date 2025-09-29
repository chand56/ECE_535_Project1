# ECE_535_Project1
# Secure PTP Time Synchronization with OP-TEE

## Motivation
Precise time is critical for safe and reliable control systems. Our project uses ARM Trustzone (OP-TEE) to isolate key vulnerable PTP functions securing trustworthy time giving us a chance to detect spoofing/delay attacks. This protocol also provides us with integrity when it comes to protected timestamps and inputs.

## Design Goals and Deliverables

Since this is a smaller version of the project we plan to focus on:

• Characterize the network delay between raspberry pi and the edge device  
• Estimate the relative clock drift between the participating devices

## System Blocks

PTP messages arrive → Linux validates through OP-TEE and requests timestamp → servo computes offset using trusted inputs → decision logged → OP-TEE tags selected PTP frames

## Hardware/Software Requirements

Windows PC, NXP i.MX6Q SabreSD development board (ARM Cortex-A9 cores), OP-TEE

## Team Member Responsibilities

Chandler Cheron - Networking, Writing includes data collection, attack simulation  
Tre Allen-Robinson - Setup, software, PTP implementation, delay measurements  
Aaron - Research, Algorithm design, TEE integration

## Project Timeline

Week 1-2: Research/Project presentation  
Week 3-4: PTP algorithm development, TEE integration  
Week 5-6: Delay and Attack testing  
Week 7-8: Writing Paper

## References

Trusted Timing Services with Timeguard, RTAS 2024  
Securing Time in Untrusted Operating Systems with TimeSeal, RTSS 2019

