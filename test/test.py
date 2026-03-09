# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# ut - unit test
# NC - Not Changed

#Test 1: Repeated frames from 0x01 - 0xFE with fvalid Always 1
@cocotb.test()
async def extract_MAC_ut(dut):
    dut._log.info("Unit Test extract_MAC (Sweep test frame: 0x01-0xFE Repeated | fvalid Always 1) Start")

    #Clock period set to 125 KHz
    clock = Clock(dut.clk, 8, units="us")
    cocotb.start_soon(clock.start())

    for i in range(0x01, 0xFF):
        dut._log.info("Reset values")
        expected = 0
        cast_type = 3
        dut.fvalid.value = 0
        dut.frame.value = 0
        dut.rst_n.value = 0
        await ClockCycles(dut.clk, 10)
        dut.rst_n.value = 1

        dut._log.info("extract_MAC Behaviour")

        dut.fvalid.value = 1
    
        dut.frame.value = i

        for val in range(6):
            expected = (expected << 8) | i

        await ClockCycles(dut.clk, 6)

        assert dut.MAC_dest.value == expected

        dut._log.info(f"Extracted MAC Address matches expectations for frame value {i}")
        
        if dut.MAC_dest.value[40] == 0 and dut.MAC_dest.value != 0xFFFFFFFFFFFF:
            cast_type = 0

            assert dut.request_t.value == cast_type
            dut._log.info("Request type matches expected value: Unicast")

        elif dut.MAC_dest.value[40] == 1 and dut.MAC_dest.value != 0xFFFFFFFFFFFF:
            cast_type = 1

            assert dut.request_t.value == cast_type
            dut._log.info("Request type matches expected value: Multicast")

        elif dut.MAC_dest.value == 0xFFFFFFFFFFFF:
            cast_type = 2

            assert dut.request_t.value == cast_type
            dut._log.info("Request type matches expected value: Broadcast")

        else:
            cast_type = 3
            
            assert dut.request_t.value == cast_type
            dut._log.info("Request type matches expected value: Reserved") 



        assert dut.mvalid.value == 1

        dut._log.info("MAC Address is complete and a valid address")


#Test 2: 0x00
@cocotb.test()
async def extract_MAC_ut(dut):
    dut._log.info("Unit Test extract_MAC (Frame: 0x00 | fvalid Always 1) Start")

    #Clock period set to 125 KHz
    clock = Clock(dut.clk, 8, units="us")
    cocotb.start_soon(clock.start())
    dut._log.info("Reset values")
    dut.fvalid.value = 0
    dut.frame.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("extract_MAC Behaviour")

    dut.fvalid.value = 1

    dut.frame.value = 0x00

    await ClockCycles(dut.clk, 6)

    assert dut.MAC_dest.value == 0x000000000000

    dut._log.info(f"Extracted MAC Address matches expectations for frame value {dut.MAC_dest.value}")
    

    assert dut.request_t.value == 0
    
    dut._log.info("Request type matches expected value: Unicast")

    assert dut.mvalid.value == 1

    dut._log.info("MAC Address is complete and a valid address")

#Test 3: 0xFF
@cocotb.test()
async def extract_MAC_ut(dut):
    dut._log.info("Unit Test extract_MAC (Frame: 0xFF | fvalid Always 1) Start")

    #Clock period set to 125 KHz
    clock = Clock(dut.clk, 8, units="us")
    cocotb.start_soon(clock.start())
    dut._log.info("Reset values")
    dut.fvalid.value = 0
    dut.frame.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("extract_MAC Behaviour")

    dut.fvalid.value = 1

    dut.frame.value = 0xFF

    await ClockCycles(dut.clk, 6)

    assert dut.MAC_dest.value == 0xFFFFFFFFFFFF

    dut._log.info(f"Extracted MAC Address matches expectations for frame value {dut.MAC_dest.value}")
    

    assert dut.request_t.value == 2
    
    dut._log.info("Request type matches expected value: Broadcast")

    assert dut.mvalid.value == 1

    dut._log.info("MAC Address is complete and a valid address")


#Test 4: Random frames from 0x00 - 0xFF with fvalid Always 1
@cocotb.test()
async def extract_MAC_ut(dut):
    dut._log.info("Unit Test extract_MAC (Sweep test frame: 0x00-0xFF Randomized | fvalid Always 1) Start")

    #Clock period set to 125 KHz
    clock = Clock(dut.clk, 8, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Reset values")
    randomized_frame = 0
    expected = 0
    cast_type = 3
    dut.fvalid.value = 0
    dut.frame.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("extract_MAC Behaviour")

    dut.fvalid.value = 1

    for val in range(6):
        randomized_frame = random.choice()
        dut.frame.value = randomized_frame

        expected = (expected << 8) | randomized_frame

        await ClockCycles(dut.clk, 1)

    assert dut.MAC_dest.value == expected

    dut._log.info(f"Extracted MAC Address matches expectated: {dut.MAC_dest.value} ")
    
    if dut.MAC_dest.value[40] == 0 and dut.MAC_dest.value != 0xFFFFFFFFFFFF:
        cast_type = 0

        assert dut.request_t.value == cast_type
        dut._log.info("Request type matches expected value: Unicast")

    elif dut.MAC_dest.value[40] == 1 and dut.MAC_dest.value != 0xFFFFFFFFFFFF:
        cast_type = 1

        assert dut.request_t.value == cast_type
        dut._log.info("Request type matches expected value: Multicast")

    elif dut.MAC_dest.value == 0xFFFFFFFFFFFF:
        cast_type = 2

        assert dut.request_t.value == cast_type
        dut._log.info("Request type matches expected value: Broadcast")

    else:
        cast_type = 3
        
        assert dut.request_t.value == cast_type
        dut._log.info("Request type matches expected value: Reserved") 



    assert dut.mvalid.value == 1

    dut._log.info("MAC Address is complete and a valid address")



#Test 5: fvalid changes to 0 during extraction process

#Test 6: Reset activated during extraction 

 


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 8 us (125 KHz)
    clock = Clock(dut.clk, 8, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.fvalid.value = 0
    dut.frame.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.frame.value = 0xAA
    dut.fvalid.value = 1

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    # dut.MAC should contain the 48-bit MAC address
    # dut.table_st should contain the 2-bit table status

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
