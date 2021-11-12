%% Handler for matlab .mat file's trial cue type, implement one for yourself if required 


clc;clear;

load('Data/data.mat'); % ~ 1GB of data
a = trialInfo.cueType;
b = trialInfo.correct;
s = trialInfo.sample;

c = zeros(size(a, 1), 1);

for i = 1:size(a, 1)
    if isequal(a{i, 1}, 'trial')
        c(i) = 1;
    end
end

save('Data/cues.mat', 'b', 'c', 's');


%%