`default_nettype none

module extract_MAC (    
    input wire i_clk,
    input wire i_rstn,
    input wire [7:0] i_frame,
    input wire i_fvalid,
    output reg [47:0] o_MAC_dest,
    output reg o_mvalid,
    output reg o_request_t [1:0]
    );
endmodule
