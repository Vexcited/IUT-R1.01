const std = @import("std");

fn input(message: []const u8) !i32 {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();

    var buffer: [1024]u8 = undefined;
    try stdout.print("{s}", .{message});

    if (try stdin.readUntilDelimiterOrEof(buffer[0..], '\n')) |user_input| {
        return std.fmt.parseInt(i32, user_input, 10);
    }

    return @as(i32, 0);
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("TP2.Ex2: Compare two integers.\n\n", .{});

    const n1 = try input("n1 = ");
    const n2 = try input("n2 = ");

    try stdout.print("\nResult : ", .{});

    if (n1 > n2) {
        try stdout.print("{d} > {d}\n", .{ n1, n2 });
    } else if (n1 < n2) {
        try stdout.print("{d} < {d}\n", .{ n1, n2 });
    } else {
        try stdout.print("{d} = {d}\n", .{ n1, n2 });
    }
}
