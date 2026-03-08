`default_nettype none

module MAC_table (
    input wire i_clk,
    input wire i_rstn,
    input wire i_mvalid,
    input wire [47:0] i_MAC_dest,

    output reg [47:0] o_MAC,
    output reg [1:0] o_table_st
);
endmodule