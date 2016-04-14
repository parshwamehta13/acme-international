function q1
    maximum_queue_length = 100;
    waitingtime = 0;
    total_process = 65;
    maximum_number_cycles = 6;
    maximum_arrival_time = 90;
    stop = 250;
    max_priority = 10;
    
    t = [0];
    length_of_queue = [0];
    processQueue = [];
    all_processes = [];
    firstTime = 1;
    
    for i=1:total_process
        temp = randi(maximum_number_cycles);
        all_processes = [all_processes; i temp randi(maximum_arrival_time) temp randi(max_priority)];
    end
    
    for i=2:stop
        t(i) = t(i-1) + 1;
        length = size(processQueue,1);
        if length<(maximum_queue_length*0.8)
            all_processes_Len = size(all_processes,1);
            j = 1;
            while j<=all_processes_Len
                if all_processes(j, 3)<=t(i) && length<(maximum_queue_length*0.8)
                    processQueue = [processQueue; all_processes(j,:)];
                    all_processes(j,:) = [];
                    length = length + 1;
                    all_processes_Len = all_processes_Len - 1;
                end
                j = j + 1;
            end
        end
             
        if length~=0
            if firstTime==1
                j = index_of_maximum_priority(processQueue);
                temp = processQueue(j,:);
                processQueue(j,:) = processQueue(1,:);
                processQueue = [temp ; processQueue];
                processQueue(2,:) = [];
                firstTime = 0;
            end
            
            processQueue(1,2) = processQueue(1,2) - 1;
            if processQueue(1,2)==0
                waitingtime = waitingtime + t(i) - (processQueue(1,3) + processQueue(1,4));
                processQueue(1,:) = [];
                length = length - 1;
                
                if length~=0
                    j = index_of_maximum_priority(processQueue);
                    temp = processQueue(j,:);
                    processQueue(j,:) = processQueue(1,:);
                    processQueue = [temp ; processQueue];
                    processQueue(2,:) = [];                    
                end
            end
        end
        length_of_queue(i) = length;
    end
    Average_Waiting_Time = waitingtime / total_process;
    plot(t,length_of_queue,'lineWidth',2);
    title('Priority Based Scheduling')
    xlabel('Number of Cycles')
    ylabel('Queue Length')
    disp(strcat('Priority, Average Waiting Time: ', num2str(Average_Waiting_Time)))
end

function y = index_of_maximum_priority(processQueue)
    len = size(processQueue);
    y = 1;
    currMin = processQueue(1,5);
    for i=1:len
        if currMin > processQueue(i,5);
            currMin = processQueue(i,5);
            y = i;
        end
    end
end