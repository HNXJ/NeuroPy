%% Handler for trial cue type

clc;clear;

load('data.mat'); % ~ 1GB of data
a = trialInfo.cueType;
c = zeros(size(a, 1), 1);

for i = 1:size(a, 1)
    if isequal(a{i, 1}, 'trial')
        c(i) = 1;
    end
end

save('cues.mat', 'c');

%%