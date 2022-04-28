#define N 100;

int count = 0;

void producer()
{
	int item;
	
	while(true)
	{
		item = produce_item();
		if(count == N)
			sleep();
		insert_item(item);
		count = count + 1;
		if(count == 1)
			wakeup(consumer);
	}
}

void consumer()
{
	int item;
	
	while(true)
	{
		if(count == 0)
			sleep();
		item = remove_item();
		count = count - 1;
		if(count == N - 1)
			wakeup(produtor);
		consume_item(item);
	}
}

