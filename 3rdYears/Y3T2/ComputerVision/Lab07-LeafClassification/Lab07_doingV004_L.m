% Initialize Storage
% outpicCollection = cell(25, 1);
% processedImages = cell(25, 1);
% outpicCollection_test = cell(15, 1);
% processedImages_test = cell(15, 1);
eps = 1e-5;

% Load Training Labels
load('trainLabel.mat');
numTrain = length(trainLabel);
featureMatrix = zeros(numTrain, 6);

% Set Paths
trainPath = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\';

% Process Training Images
for i = 1:numTrain
    filename = fullfile(trainPath, [num2str(i) '.jpg']);
    im = imread(filename);
    grayImage = rgb2gray(im);

    % Reduce illumination effects
    shadePattern = imboxfilt(grayImage, 51);  
    outpic = double(grayImage) ./ double(shadePattern);
    % subplot(1, 3, 1);
    % imshow(outpic);
    
    % Apply Gaussian filter
    gauss_im = imgaussfilt(outpic, 5);
    % subplot(1, 3, 2);
    % imshow(gauss_im);
    
    % Binarization & Morphological Processing
    level = graythresh(gauss_im);
    bw = ~imbinarize(gauss_im, level);
    bw = imfill(bw, 'holes');
    % subplot(1, 3, 3);
    % imshow(bw);

    % Extract Features from the largest object
    stats = regionprops(bw, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Orientation');
    if ~isempty(stats)
        % Select the largest region
        [~, maxIdx] = max([stats.Area]);
        stats = stats(maxIdx);
        
        featureVector = [stats.Perimeter, stats.Area, stats.Eccentricity, ...
                         stats.MajorAxisLength, stats.MinorAxisLength, stats.Orientation];
    else
        featureVector = zeros(1, 6);
    end
    
    featureMatrix(i, :) = featureVector;
end

% Normalize Features
meanFeature = mean(featureMatrix, 1);
stdFeature = std(featureMatrix, 1);
featureMatrix = (featureMatrix - meanFeature) ./ (stdFeature + eps); % Avoid division by zero

% Train Classifier
Mdl = fitcecoc(featureMatrix, trainLabel);

% Load Test Labels
load('testLabel.mat');
numTest = length(testLabel);
featureMatrix_test = zeros(numTest, 6);

testPath = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\';

% Process Test Images
for i = 1:numTest
    filename_test = fullfile(testPath, [num2str(i) '.jpg']);
    im_test = imread(filename_test);
    grayImage_test = rgb2gray(im_test);

    % Reduce illumination effects
    shadePattern_test = imboxfilt(grayImage_test, 51);
    outpic_test = double(grayImage_test) ./ double(shadePattern_test);

    % Apply Gaussian filter
    gauss_im_test = imgaussfilt(outpic_test, 5);

    % Binarization & Morphological Processing
    level_test = graythresh(gauss_im_test);
    bw_test = ~imbinarize(gauss_im_test, level_test);
    bw_test = imfill(bw_test, 'holes');

    % Extract Features from the largest object
    stats_test = regionprops(bw_test, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Orientation');
    if ~isempty(stats_test)
        [~, maxIdx] = max([stats_test.Area]);
        stats_test = stats_test(maxIdx);

        featureVector_test = [stats_test.Perimeter, stats_test.Area, stats_test.Eccentricity, ...
                              stats_test.MajorAxisLength, stats_test.MinorAxisLength, stats_test.Orientation];
    else
        featureVector_test = zeros(1, 6);
    end

    % outpicCollection_test{i} = featureVector_test;
    % processedImages_test{i} = bw_test;
    
    featureMatrix_test(i, :) = featureVector_test;
end

% Normalize Test Features
featureMatrix_test = (featureMatrix_test - meanFeature) ./ (stdFeature + eps);

% Predict Labels
predictedLabels = predict(Mdl, featureMatrix_test);

% Display Results
resultsTable = table(testLabel(:), predictedLabels(:), 'VariableNames', {'TrueLabels', 'PredictedLabels'});
disp(resultsTable);

% Confusion Matrix
figure(3);
cm = confusionchart(testLabel, predictedLabels);
cm.Title = 'Confusion Matrix - Leaf Classification';