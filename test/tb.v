`default_nettype none
`timescale 1ns / 1ps

/* This testbench just instantiates the module and makes some convenient wires
   that can be driven / tested by the cocotb test.py.
*/
module tb ();

  // Dump the signals to a VCD file. You can view it with gtkwave or surfer.
  initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, tb);
    #1;
  end

  // Wire up the inputs and outputs:
  reg clk;
  reg rst_n;
  reg [7:0] frame;
  reg fvalid;
  wire [47:0] MAC;
  wire [1:0] table_st;

  // Instantiate control_MAC_learning:
  control_MAC_learning user_project (
      .i_clk    (clk),        // clock
      .i_rstn   (rst_n),      // not reset
      .i_frame  (frame),      // 8-bit frame input
      .i_fvalid (fvalid),     // frame valid
      .o_MAC    (MAC),        // 48-bit MAC address output
      .o_table_st(table_st)   // 2-bit table status output
  );

endmodule
