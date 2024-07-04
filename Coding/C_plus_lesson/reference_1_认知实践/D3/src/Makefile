OBJS = pstring.o

../libpstring.a : $(OBJS)
	ar rcs ../libpstring.a $(OBJS)

$(OBJS) : pstring.c ../pstring.h
	gcc -c pstring.c ../pstring.h -I../
