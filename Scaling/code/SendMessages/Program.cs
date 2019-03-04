using System;
using System.Collections.Generic;
using Amazon.SQS.Model;
using Amazon.SQS;
using System.Threading.Tasks;
using System.Linq;

namespace send
{
    class Program
    {

     	static void Main(string[] args)
        {
            MainAsync(args).GetAwaiter().GetResult();
        }

        private static async Task MainAsync(string[] args)
        {
            var sqsClient = new Amazon.SQS.AmazonSQSClient();
            for (var idx = 0; idx <=50000; idx++ )
            {
             	Console.WriteLine(String.Format("BATCH No.: {0}",idx));
                var sendMessageBatchRequest = new SendMessageBatchRequest
                {
                    Entries = generateMessages(),
                    QueueUrl = "https://sqs.eu-west-1.amazonaws.com/655379451354/4developers_queue"
                };
                var resonse = await sqsClient.SendMessageBatchAsync(sendMessageBatchRequest);
            }
        }

	    private static List<SendMessageBatchRequestEntry> generateMessages()
        {
            var messages = new List<SendMessageBatchRequestEntry>();
            for (var idx = 1; idx <= 10; idx++)
            {
             	var uuid = System.Guid.NewGuid().ToString();
                //Console.WriteLine(uuid);
                var message = new SendMessageBatchRequestEntry(uuid, "Message");
                messages.Add(message);
            }
            return messages;
        }

    }
}