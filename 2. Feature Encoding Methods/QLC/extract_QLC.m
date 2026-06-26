clc;
clear all;
feature_QLC=[];

[data, sequence] = fastaread('ACP-Training.txt')
Total_Seq_train=size(sequence,2);

for i=1:(Total_Seq_train)
    i
    SEQ=sequence(i);
	FF=mctd(SEQ);
    SEQ=cell2mat(SEQ);
    feature_QLC(i,:)=FF;
end
ACPs_QLC_Training=[feature_QLC];
save ACPs_QLC_Training ACPs_QLC_Training;
csvwrite('ACPs_QLC_Training.csv',ACPs_QLC_Training);
