![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# UWASIC W26: MAC learning table

## Getting Started

1. Clone this repository
2. Update [info.yaml](info.yaml) with your project details
3. Make a post in the [UWASIC Discord server](https://discord.gg/ZcfXmCkV) under **#onboarding/posts** to kick things off!
4. [Read the full documentation and specifications here](https://docs.uwasic.com/doc/mac-learning-table-IvSuOxHSn4)

## Disclaimer

The final implementation will be integrated into an FPGA fabric of a larger SoC. This TinyTapeout template serves as a trackable starting point for initial prototyping and team training purposes.

## Set up your Verilog project

1. Add your Verilog files to the `src` folder.
2. Edit the [info.yaml](info.yaml) and update information about your project, paying special attention to the `source_files` and `top_module` properties. 
3. Edit [docs/info.md](docs/info.md) weekly and document your weekly progress on RTL and Verification, along with any comments or concerns you may have.

The GitHub action will automatically build the ASIC files using [OpenLane](https://www.zerotoasiccourse.com/terminology/openlane/).

## Writing cocotb Testbenches

This project has a hierarchical design structure:
- **`MAC_learning`** (final top module): Complete MAC learning system
  - **`control_MAC_learning`** (primary verification target): MAC learning controller with frame processing
    - **`MAC_table`** (submodule): MAC table memory and management logic
    - **`extract_MAC`** (submodule): MAC address extraction from valid frames

**For the first phase of verification, the testbench instantiates `control_MAC_learning` as the top hierarchy.** This allows you to thoroughly verify the core controller logic, frame processing, and MAC extraction before integrating into the full `MAC_learning` module. The test file `test/test.py` contains cocotb test cases that drive the testbench and verify:
- Frame processing and MAC extraction logic
- MAC table state transitions
- Proper output of MAC addresses and table status

> **Note:** If you're more comfortable using Verilog or SystemVerilog testbenches for verification, feel free to use those instead of cocotb.

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [Documentation](https://docs.uwasic.com/doc/mac-learning-table-IvSuOxHSn4)
- [UWASIC discord server](https://discord.gg/ZcfXmCkV)
