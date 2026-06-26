%% Code to extract the RECM_LPQ & RECM_DWT
clear all
clc;
[data, sequence]= fastaread('ACP_training.txt');

Total_Seq_train=size(sequence,2);
for i=1:(Total_Seq_train)
     i
    SEQ=sequence(i);
    SEQ=cell2mat(SEQ);
    RECM_T = RECMT(SEQ);
    RECM_T=RECM_T';
    P = uint8(255 * mat2gray(RECM_T));
    
	%%%%%%%%%%%% LPQ %%%%%%%%%%%%%%%%
   FF=Process_LPQ(P);
    RECM_LPQ_ACP_training(i,:)=FF;
    
   %%%%%%%%%%%% DWT %%%%%%%%%%%%%%%%
     FF=GetDWT(P);
     RECM_DWT_ACP_training(i,:)=FF;
    
   end


save RECM_LPQ_ACP_training RECM_LPQ_ACP_training;
save RECM_DWT_ACP_training RECM_DWT_ACP_training;
%%%% To Create CSV sheet for the data %%%%%%%%%
   
csvwrite('RECM_LPQ_ACP_training.csv',RECM_LPQ_ACP_training);
csvwrite('RECM_DWT_ACP_training.csv',RECM_DWT_ACP_training);
