`default_nettype none

module control_MAC_learning (
    input wire i_clk,
    input wire i_rstn,
    input wire [7:0] i_frame,
    input wire i_fvalid,
    output reg [47:0] o_MAC,
    output reg [1:0] o_table_st
);

endmodule