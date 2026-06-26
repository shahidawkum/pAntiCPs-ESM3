function RECM_T = RECMT(AAS)

load RECM.mat;
type = 20;

PT = [];
L = length(AAS);
for i = 1:L
    switch AAS(i)
        case {'A', 'a'}
             PT = [PT;RECM(1,:)];
        case {'C', 'c'}
            PT = [PT;RECM(2,:)];
        case {'D', 'd'}
            PT = [PT;RECM(3,:)];
        case {'E', 'e'}
            PT = [PT;RECM(4,:)];
        case {'F', 'f'}
            PT = [PT;RECM(5,:)];
        case {'G', 'g'}
            PT = [PT;RECM(6,:)];
        case {'H', 'h'}
            PT = [PT;RECM(7,:)];
        case {'I', 'i'}
            PT = [PT;RECM(8,:)];
        case {'K', 'k'}
            PT = [PT;RECM(9,:)];
        case {'L', 'l'}
            PT = [PT;RECM(10,:)];
        case {'M', 'm'}
            PT = [PT;RECM(11,:)];
        case {'N', 'n'}
            PT = [PT;RECM(12,:)];
        case {'P', 'p'}
            PT = [PT;RECM(13,:)];
        case {'Q', 'q'}
            PT = [PT;RECM(14,:)];
        case {'R', 'r'}
            PT = [PT;RECM(15,:)];
        case {'S', 's'}
            PT = [PT;RECM(16,:)];
        case {'T', 't'}
            PT = [PT;RECM(17,:)];
        case {'V', 'v'}
            PT = [PT;RECM(18,:)];
        case {'W', 'w'}
            PT = [PT;RECM(19,:)];
        case {'Y', 'y'}
            PT = [PT;RECM(20,:)];
    end
end
RECM_T = PT;