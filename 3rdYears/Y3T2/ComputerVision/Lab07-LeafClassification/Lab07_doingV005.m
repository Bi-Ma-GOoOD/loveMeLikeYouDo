% Initialize Storage
outpicCollection = cell(25, 1);
processedImages = cell(25, 1);
outpicCollection_test = cell(15, 1);
processedImages_test = cell(15, 1);
eps = 1e-7;

% Load Training Labels
load('trainLabel.mat');
numTrain = length(trainLabel);
featureMatrix = zeros(numTrain, 10); % Now using 10 features

% Set Paths
trainPath = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\';

% Process Training Images
for i = 1:numTrain
    filename = fullfile(trainPath, [num2str(i) '.jpg']);
    im = imread(filename);
    grayImage = rgb2gray(im);

    % Adaptive Illumination Correction
    filterSize = max(21, round(min(size(grayImage)) * 0.1));  % Adaptive window size
    shadePattern = imboxfilt(grayImage, filterSize);  
    outpic = double(grayImage) ./ double(shadePattern);
    
    % Adaptive Thresholding
    bw = ~imbinarize(outpic, adaptthresh(outpic, 0.4));
    
    % Morphological Processing
    bw = imfill(bw, 'holes');
    bw = bwareaopen(bw, 100); % Remove small objects

    % Extract Features from the largest object
    stats = regionprops(bw, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', ...
                        'MinorAxisLength', 'Orientation', 'Solidity', 'Extent', 'ConvexArea');
    
    if ~isempty(stats)
        % Select the largest region
        [~, maxIdx] = max([stats.Area]);
        stats = stats(maxIdx);
        
        % Compute Circularity = (4π * Area) / (Perimeter^2)
        Circularity = (4 * pi * stats.Area) / (stats.Perimeter^2);
        
        % New Feature Vector
        featureVector = [stats.Perimeter, stats.Area, stats.Eccentricity, ...
                         stats.MajorAxisLength, stats.MinorAxisLength, stats.Orientation, ...
                         stats.Solidity, stats.Extent, stats.ConvexArea, Circularity];
    else
        featureVector = zeros(1, 10);
    end

    outpicCollection{i} = featureVector;
    processedImages{i} = bw;
    
    featureMatrix(i, :) = featureVector;
end

% Normalize Features
meanFeature = mean(featureMatrix, 1);
stdFeature = std(featureMatrix, 1);
featureMatrix = (featureMatrix - meanFeature) ./ (stdFeature + eps);

% Train Classifier (Using Ensemble for better accuracy)
Mdl = fitcensemble(featureMatrix, trainLabel, 'Method', 'Bag');

% Load Test Labels
load('testLabel.mat');
numTest = length(testLabel);
featureMatrix_test = zeros(numTest, 10);

testPath = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\';

% Process Test Images
for i = 1:numTest
    filename_test = fullfile(testPath, [num2str(i) '.jpg']);
    im_test = imread(filename_test);
    grayImage_test = rgb2gray(im_test);

    % Adaptive Illumination Correction
    shadePattern_test = imboxfilt(grayImage_test, filterSize);
    outpic_test = double(grayImage_test) ./ double(shadePattern_test);

    % Adaptive Thresholding
    bw_test = ~imbinarize(outpic_test, adaptthresh(outpic_test, 0.4));

    % Morphological Processing
    bw_test = imfill(bw_test, 'holes');
    bw_test = bwareaopen(bw_test, 100);

    % Extract Features
    stats_test = regionprops(bw_test, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', ...
                             'MinorAxisLength', 'Orientation', 'Solidity', 'Extent', 'ConvexArea');

    if ~isempty(stats_test)
        [~, maxIdx] = max([stats_test.Area]);
        stats_test = stats_test(maxIdx);

        Circularity_test = (4 * pi * stats_test.Area) / (stats_test.Perimeter^2);

        featureVector_test = [stats_test.Perimeter, stats_test.Area, stats_test.Eccentricity, ...
                              stats_test.MajorAxisLength, stats_test.MinorAxisLength, stats_test.Orientation, ...
                              stats_test.Solidity, stats_test.Extent, stats_test.ConvexArea, Circularity_test];
    else
        featureVector_test = zeros(1, 10);
    end

    outpicCollection_test{i} = featureVector_test;
    processedImages_test{i} = bw_test;
    
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
cm.ColumnSummary = 'column-normalized';
cm.RowSummary = 'row-normalized';
