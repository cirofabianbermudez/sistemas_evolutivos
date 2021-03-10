# Makefile for compiling NSGA-II source code
CC=gcc
LD=gcc
RM=rm -f
CFLAGS=-Wall
# CFLAGS=-Wall -Werror -ansi -pedantic -I/usr/include/python2.7/
# LDFLAGS= -g
# LDFLAGS= -L/usr/lib/python2.7/config/
# CFLAGS=-Wall -Werror -ansi -pedantic
OBJS:=$(patsubst %.c,%.o,$(wildcard *.c))
MAIN=nsga2r
all:$(MAIN)
$(MAIN):$(OBJS)
	# $(LD) $(LDFLAGS) $(OBJS) -o $(MAIN) -lm -lpython2.7
	$(LD) $(LDFLAGS) $(OBJS) -o $(MAIN) -lm
%.o: %.c global.h rand.h
	$(CC) $(CFLAGS) -c $<
clean:
	$(RM) $(OBJS)


