`default_nettype none

module control_MAC_learning (
    input wire i_clk,
    input wire i_rstn,
    input wire [7:0] i_frame,
    input wire i_fvalid,
    output reg [47:0] o_MAC,
    output reg [1:0] o_table_st
);

    extract_MAC extraction_sub_module(
        .i_clk(i_clk),
        .i_rstn(i_rstn),
        .i_frame(i_frame),
        .i_fvalid(ifvalid),
        .o_mvalid(o_to_i_mvalid),
        .o_MAC_dest(o_to_i_MAC_dest),
        .o_request_t(temp_o_request_t)
    );

    wire[1:0] temp_o_request_t;

    wire o_to_i_mvalid;
    wire[47:0] o_to_i_MAC_dest;

    MAC_table(
        .i_clk(i_clk),
        .i_rstn(i_rstn),
        .i_mvalid(o_to_i_mvalid),
        .o_MAC(o_MAC),
        .o_table_st(o_table_st)
    )

endmodule