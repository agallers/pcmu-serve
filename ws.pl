#!/usr/bin/perl -w
use strict;
use warnings;
use Net::WebSocket::Server; # cpanm Net::WebSocket::Server (https://metacpan.org/pod/Net::WebSocket::Server)

## config
my $port = 6120; 
my $filename = 'K04SynBass.ulaw'; # mu-law file

## Read audio
my @g711 = ();
open(my $fh, '<:raw', $filename) or die "could not open $@\n";
while (read($fh, my $buf, 800)) { # (800 samples) / (8000 samples/sec) = .1 seconds of audio
	push(@g711, $buf);
}
close($fh);
print "Read " . scalar(@g711) . " blocks of 800 from file $filename\n";

## Run server 
my $i = 0;
my $ws = Net::WebSocket::Server->new(
	listen => $port,
	tick_period => .1, # sending 800samples == .1 seconds of audio every .1 seconds
	on_tick => sub {
		my ($serv) = @_;
		return unless $serv->connections;
		print "Sending 800 samples (time: " . time . ", index $i)\n";
		$_->send_binary($g711[$i]) for $serv->connections;
		$i = 0 if ++$i == scalar(@g711);
	},
)->start();

