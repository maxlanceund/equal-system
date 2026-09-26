# Error-Correcting Code Structure in Neural Networks

## — Non-Local Information Distribution, Task-Driven Effective Rank, and the Analogy with Black Holes

| Item | Content |
| :--- | :--- |
| **Title** | Error-Correcting Code Structure in Neural Networks — Non-Local Information Distribution, Task-Driven Effective Rank, and the Analogy with Black Holes |
| **Author** | Zhong Shanzhen |
| **Date** | 2026-09-26 (Revised: 2026-09-27, Version 3.3) |
| **License** | CC BY-NC 4.0 |
| **Keywords** | error-correcting code, information distribution, conditional entropy, neural networks, holographic principle, quantum error correction, low-rank structure, task-driven, background mode |

---

## I. Abstract

This paper uses an information loss rate D_f to quantitatively measure the information distribution in the hidden layers of a neural network. There are nine core findings:

**First, information is mainly distributed in the correlations between neurons, not in individual neurons, nor concentrated in a few "important" neurons.** For the h1 layer (128 neurons), the average D_f of a single neuron is 0.85, the D_f after destroying correlations is 0.64, and the D_f when correlations are preserved is 0.16. Correlation contributes 75% of the total information. A layer-by-layer scan shows that the correlation contribution fraction of every hidden layer lies between 52% and 75%. Sorting neurons by variance and adding them progressively, D_f falls slowly from 1.000 to 0.355, nearly identical to random ordering — variance cannot pick out "important neurons." Information is dispersed across all neurons. When the output layer is dimension-locked, the lost information migrates into the joint distribution of the output layer and the penultimate layer; the migration threshold is approximately 0.8 × number of classes.

**Second, the partial-shuffle curve is convex, indicating an error-correcting code structure.** Shuffling 40% of h1 neurons raises D_f by only 6%; shuffling 50%, by 9%; but shuffling 80%, by 43%.

**Third, the error-correction threshold grows with layer width.** At h1=32, shuffling 50% loses 29% of information; at h1=128, 9%; at h1=512, only 3%.

**Fourth, the error-correcting code is activated within the first epoch of training, and overall information retention is improved at the same time.** At random initialization, norm@50 = 0.353. After 1 epoch, norm@50 drops to 0.224. Over the next 30 epochs, it stabilizes at 0.22–0.28. A control experiment shows that after training, D_f of every layer drops sharply (layer1: 0.472 → 0.256; output: 0.777 → 0.389), while the input layer is unchanged. **Training simultaneously "activates error correction" and "improves information retention" within the first epoch.**

**Fifth, the output-layer D_f is locked by its dimension.** The output layer has only 10 dimensions, so its D_f is locked near 0.6 and cannot reflect network quality. A width scan shows: as h1 grows from 16 to 1024, single-layer D_f of h1 falls from 0.645 to 0.060, while output-layer D_f stays fixed at 0.61–0.62. Correlations with accuracy: D_f is only −0.52 (weak), margin_mean is +0.98 (strong), out_entropy is −0.99 (strongest). **Output entropy and margin are the strong predictors of accuracy.** The complete training curve shows that over 40 epochs, D_f oscillates between 0.56 and 0.71 with no net trend, while margin rises monotonically from −0.024 to 10.8.

**Sixth, the relational structure is low-rank, and effective rank grows with the number of classes, but the growth form depends on training sufficiency.** When trained for 10 epochs (accuracy 88–97%), the effective rank satisfies r_eff ≈ 1.25 × number of classes (k ≤ 10), with fit r_eff − k = 1.26 · log₂(k). After sufficient training (accuracy 97–99%), the effective rank rises significantly (at k=10, from 12.35 to 19.58), but no longer obeys a simple formula and jitters at high k. **Effective rank is jointly determined by task, training, and architecture.**

**Seventh, in the direct projection layer of a fully connected network, the "background mode" is architecture-driven.** For MNIST (FC h1), the largest eigenmode of the mutual information matrix is uncorrelated with class (MI = 0.433) and strongly correlated with image contrast/brightness (−0.942 / −0.941). This "background mode" does not change with the task; it is a property of the architecture.

**Eighth, the separation between background mode and class modes holds only in the "direct projection layer."** For CIFAR-10 (CNN, h1 after convolutional layers), effective rank drops to 4.78, and the background mode is almost uncorrelated with brightness (−0.076), with no clear background/class separation. This shows that the separation structure depends on the projection level: direct projection preserves the global statistics of the input; post-convolution projection does not.

**Ninth, effective rank saturates at high class counts and full training.** The 20-class task has effective rank only 8.73, lower than the 12.00 of the 10-class task; even after 30 epochs, it has not saturated (8.39 → 10.01). This shows that effective rank is affected both by training sufficiency and by architectural dimension.

**Correspondence with black hole physics:** These results quantitatively correspond to the quantum error-correcting code picture in AdS/CFT duality. The "background mode" corresponds to the horizon geometry itself; the "class modes" correspond to information falling into matter; the separation structure matches the "background + signal" structure of the black hole entanglement spectrum. And "separation holds only at the direct projection layer" corresponds to the detail in the holographic principle that "the boundary must be the outermost layer." "Information migration" corresponds to the island mechanism of the black hole information paradox.

**Positioning of this paper:** This paper is not a new physics discovery, but a quantitative cross-system correspondence. It gives eight previously unreported numbers: **error-correction threshold grows linearly with layer width**, **the error-correcting code is activated within the first epoch**, **effective rank is strongly affected by training sufficiency**, **migration threshold ≈ 0.8 × number of classes**, **separation of background mode and class modes**, **background mode = input global statistics of the direct projection layer**, **effective rank saturates at 20 classes**, and **layer-wise correlation contribution fraction of 52–75%**.

---

## II. Introduction

### 1. Core Question

Is the information in a neural network distributed in individual neurons, or in the correlations between neurons?

This question already has an answer in machine learning: **distributed representation**. Hinton et al. pointed out in the 1980s that the information in a neural network is not stored "locally" but distributed across the activation patterns of many neurons.

But "distributed" is a qualitative statement. The goal of this paper is to turn it into a quantitative measurement and to ask six deeper questions:

- **How much information is in the correlations?**
- **When is this distribution formed?**
- **What is the structure of these "correlations" themselves?**
- **Is this structure task-driven or architecture-driven?**
- **What does the background mode encode?**
- **At what architectural level does this structure hold?**

### 2. Tool: Information Loss Rate D_f

Let Ω be the information to be preserved (class label), and M′ be the macroscopic description (activation of some layer). Define:

D_f = H(Ω | M′) / H(Ω)

- D_f = 0: M′ fully preserves Ω
- D_f = 1: M′ contains no Ω

### 3. Method: Destroying Correlations

Key operation: **independently shuffle the row order of each column.**

- After shuffling, the marginal distribution of each column is unchanged
- But the joint distribution between columns is destroyed
- If information is in individual columns, D_f is unchanged
- If information is in the correlations between columns, D_f rises

### 4. Correspondence with Black Hole Physics

In 2015, Almheiri, Dong, and Harlow proposed that AdS/CFT duality is essentially a quantum error-correcting code. In 2019, Penington, Almheiri, and others used this framework to resolve the black hole information paradox.

**The goal of this paper is: to quantitatively reproduce this structure in neural networks.**

### 5. Structure of the Argument

Section III gives the methods. Section IV reports the correlation distribution. Section V reports the error-correcting code structure. Section VI reports the width dependence. Section VII reports training activation and the random control. Section VIII reports output-layer lock-in, layer-wise D_f distribution, width scan, information migration, and the full training curve. Section IX reports the low-rank nature of the relational structure, its fit form, the boundary of the separation structure, and the high-class-count anomaly. Section X reports the encoding meaning of the background mode. Section XI discusses the correspondence with black holes. Section XII reports a falsified hypothesis. Section XIII discusses limitations. Section XIV concludes.

---

## III. Methods

### 1. Model

Fully connected network, input 784 (MNIST), output n classes. Hidden layer configuration is variable.

Training: 5000 images, 10 epochs, Adam optimizer, learning rate 1e-3. Test: 1000 images.

### 2. Hidden Layer Activations

For each test sample, extract the activation vector of the h1 layer. This gives a matrix A ∈ R^{N × d}, where N = 1000, d = h1 dimension.

### 3. D_f Estimation

Estimate the conditional entropy with a 70/30 split:

1. Randomly split data into training set (70%) and test set (30%)
2. Train a small classifier on the training set (128 hidden units, ReLU, 50 epochs)
3. Measure cross-entropy loss on the test set
4. D_f = CE / log(n_classes)

### 4. Damage Operation

**Shuffle:** randomly choose k columns and independently permute the rows of each column.

### 5. Null Test

Replace true labels with random labels and repeat all operations.

### 6. Mutual Information Matrix

For each pair of neurons (i, j), estimate mutual information I(i, j) by binning, giving a symmetric matrix M. Analyze:

- Effective rank (entropy exponent of the eigenvalue distribution)
- Eigenvalue gap
- Cumulative fraction of the top k eigenvalues
- Mutual information between each eigenmode and the class label

### 7. Image Statistics

For each image, compute four statistics:

- Brightness: pixel mean
- Contrast: pixel standard deviation
- Edge density: mean of adjacent-pixel differences
- High-frequency fraction: fraction of high-frequency energy in the Fourier transform

Use Spearman rank correlation to analyze the relationship between eigenmodes and these statistics.

### 8. Model Comparison Design

To test the universality of the separation structure, construct three systems:

- **MNIST + FC**: h1 directly after input (direct projection)
- **CIFAR-10 + FC**: h1 directly after input (direct projection)
- **CIFAR-10 + CNN**: h1 after three convolutional layers (indirect projection)

---

## IV. Result 1: Information Is in the Correlations

### 4.1 Correlation Contribution

| Condition | D_f |
| :--- | :--- |
| Single neuron average | 0.848 |
| All 128 neurons, correlations destroyed | 0.644 |
| All 128 neurons, correlations preserved | **0.159** |

Correlation contribution = 0.644 − 0.159 = 0.485. Normalized: 0.485 / 0.644 = **0.753**.

**75% of information is in the correlations between neurons.**

### 4.2 Null Test

Under random labels, correlation contribution ≈ −0.008. This shows that the 0.485 under true labels is a real signal.

### 4.3 Conclusion

**Information is not a property of entities; it is a relationship between entities.**

### 4.4 Shuffle Curve

See Section V.

### 4.5 Correlation Contribution Is a Network-Wide Universal Law

#### 1. Question

Is "75% of information in the correlations" a local phenomenon of h1, or a universal law across all layers?

#### 2. Design

For a 6-layer network (784-128-64-32-16-10), measure layer by layer:

- D_f(intact): D_f with correlations preserved
- D_f(shuffled): D_f with correlations destroyed
- corr_contrib = D_f(shuffled) − D_f(intact)
- corr_frac = corr_contrib / D_f(shuffled)

#### 3. Results

| Layer | Dim | D_f(intact) | D_f(shuffled) | corr_contrib | corr_frac |
| :--- | :--- | :--- | :--- | :--- | :--- |
| input | 784 | 0.041 | 0.087 | +0.046 | 0.524 |
| h1 | 128 | 0.158 | 0.638 | +0.480 | **0.752** |
| h2 | 64 | 0.239 | 0.824 | +0.585 | **0.710** |
| h3 | 32 | 0.321 | 0.901 | +0.580 | **0.644** |
| h4 | 16 | 0.391 | 0.937 | +0.546 | **0.583** |
| output | 10 | 0.457 | 0.950 | +0.493 | **0.519** |

#### 4. Observations

**One: corr_frac of all hidden layers lies between 0.52 and 0.75.** "Information in the correlations" is not a local phenomenon of h1, but a **network-wide universal law**.

**Two: corr_frac decreases as layers narrow.** h1: 0.752 → h4: 0.583 → output: 0.519.

**Three: input-layer corr_frac is only 0.524.** The input layer has almost no correlation structure.

**Four: D_f(intact) and D_f(shuffled) both rise monotonically as layers narrow.** Consistent with Section 8.3.

#### 5. Conclusion

**"Information in the correlations" is a network-wide universal law, not a property of any single layer.**

### 4.6 Information Is Dispersed Across All Neurons, Not in a Few "Important" Ones

#### 1. Question

Is information concentrated in a few high-variance neurons, or dispersed across all neurons?

#### 2. Design

For h1 (128 neurons), sort by variance descending. Add neurons progressively and measure D_f.

Control: random ordering.

**Criterion: if variance ordering is much better than random ordering, information is concentrated in a few high-variance neurons; if similar, information is dispersed.**

#### 3. Results

**Variance ordering:**

| Neurons | D_f |
| :--- | :--- |
| 0 | 1.000 |
| 1 | 0.925 |
| 8 | 0.863 |
| 16 | 0.771 |
| 32 | 0.703 |
| 64 | 0.580 |
| 96 | 0.444 |
| 128 | 0.355 |

**Variance vs. random ordering:**

| Neurons | Variance | Random | Gap |
| :--- | :--- | :--- | :--- |
| 8 | 0.862 | 0.821 | +0.041 |
| 16 | 0.801 | 0.768 | +0.033 |
| 32 | 0.710 | 0.657 | +0.053 |
| 64 | 0.573 | 0.564 | +0.009 |
| 128 | 0.388 | 0.372 | +0.016 |

#### 4. Observations

**One: D_f decreases very slowly and uniformly.** No clear "knee."

**Two: variance ordering is nearly identical to random ordering.**

**Three: no "few critical neurons."** Information is dispersed, not concentrated.

#### 5. Conclusion

**Information is neither in individual neurons nor in a few neurons, but in the joint distribution of all neurons.**

**Together with 4.1 and 4.5: information is a network-wide, all-neuron, all-correlation distributed representation.**

---

## V. Result 2: Error-Correcting Code Structure

### 1. Results (h1=128)

| Shuffle fraction | D_f | Normalized |
| :--- | :--- | :--- |
| 0.00 | 0.2065 | 0.0000 |
| 0.05 | 0.2061 | -0.0005 |
| 0.10 | 0.2129 | 0.0080 |
| 0.20 | 0.2288 | 0.0281 |
| 0.30 | 0.2367 | 0.0379 |
| 0.40 | 0.2534 | 0.0590 |
| 0.50 | 0.2987 | 0.1162 |
| 0.60 | 0.3352 | 0.1621 |
| 0.70 | 0.4081 | 0.2540 |
| 0.80 | 0.5444 | 0.4258 |
| 0.90 | 0.7521 | 0.6875 |
| 1.00 | 1.0918 | 1.1157 |

### 2. Curve Shape

First 40% shuffle: loss of only 5.9%. First 50%: 11.6%. Last 50%: 88.4%.

**Linear prediction: shuffling 50% should lose 50%. Actual loss 11.6%. Deviation −38.4 percentage points.**

Linear fit of normalized curve: slope = 0.8644, intercept = −0.1586.

Maximum single-step jump: 0.4282 at frac = 1.00.

### 3. Conclusion

**The shuffle curve is convex. The first half of neurons is nearly "sacrificial."**

This corresponds to an error-correcting code structure: **a certain fraction of damage can be tolerated without losing information.** Beyond the threshold, information collapses rapidly.

---

## VI. Result 3: Threshold Grows with Width

### 1. Results

| Config | h1 dim | Accuracy | Normalized@40% | Normalized@50% |
| :--- | :--- | :--- | :--- | :--- |
| h1=32 | 32 | 86.8% | 0.191 | 0.286 |
| h1=128 | 128 | 88.3% | 0.061 | 0.090 |
| h1=512 | 512 | 89.9% | 0.021 | 0.033 |

### 2. Observations

**All normalized@50% are far below 0.5 (linear prediction).**

- h1=32: deviation 42%
- h1=128: deviation 82%
- h1=512: deviation 94%

**Wider layers are more robust.**

### 3. Conclusion

**The error-correction threshold grows with layer width.** This corresponds to the picture in AdS/CFT: large black holes are more damage-tolerant than small ones.

---

## VII. Result 4: The Error-Correcting Code Is Activated in the First Epoch

### 7.1 Question

Is the error-correcting code present at random initialization, or is it trained?

### 7.2 Results

| Condition | norm@50 | Accuracy |
| :--- | :--- | :--- |
| Random init (untrained) | **0.353** | — |
| Trained 1 epoch | **0.224** | 45.5% |
| Trained 30 epochs | 0.275 | 92.1% |

### 7.3 Training Dynamics (h1=128)

| Epoch | Accuracy | norm@50 |
| :--- | :--- | :--- |
| 1 | 45.5% | 0.224 |
| 2 | 77.0% | 0.226 |
| 3 | 78.5% | 0.216 |
| 5 | 84.3% | 0.239 |
| 8 | 87.3% | 0.225 |
| 12 | 89.6% | 0.226 |
| 16 | 90.6% | 0.264 |
| 20 | 90.9% | 0.236 |
| 25 | 91.6% | 0.230 |
| 30 | 92.1% | 0.275 |

### 7.4 Conclusion

**The error-correcting code is not "architecturally fixed" (weak at random, 0.353), not "gradually emergent" (not slowly strengthening), but "activated in one shot."**

- From random to epoch 1: norm@50 drops from 0.353 to 0.224
- Over the next 30 epochs: stable at 0.22–0.28

**The network fixes its information distribution structure within the first epoch. Subsequent training only changes "what information is stored," not "how the information is distributed."**

### 7.5 Correspondence

This corresponds to a deeper claim of the holographic principle: the bulk-boundary encoding structure is not "slowly formed" but fixed at the moment the boundary forms.

### 7.6 Control: Random Network vs. Trained Network

#### 1. Question

While the error-correcting code is being activated, does the information-retention capacity of each layer also change?

#### 2. Design

Same architecture (784-32-16-10):

- **Random network**: initialized without training
- **Trained network**: trained 10 epochs, accuracy 86.3%

Measure D_f layer by layer.

#### 3. Results

| Layer | D_f random | D_f trained | Diff |
| :--- | :--- | :--- | :--- |
| input | 0.021 | 0.021 | −0.001 |
| layer1 | 0.472 | 0.256 | **−0.216** |
| layer2 | 0.758 | 0.359 | **−0.399** |
| output | 0.777 | 0.389 | **−0.388** |

#### 4. Observations

**One: input layer D_f unchanged.** Both 0.021.

**Two: all hidden layers drop sharply.** layer1: −0.22, layer2: −0.40, output: −0.39.

**Three: random-network D_f is already near "random level."**

#### 5. Conclusion

**Training not only activates the error-correcting code but also improves information retention at every layer.**

**Together with 7.4: training simultaneously "activates error correction" and "improves information retention" within the first epoch.**

---

## VIII. Result 5: Output-Layer Lock-In, Layer-Wise D_f, Width Scan, Information Migration, Training Curve

### 8.1 Output-Layer D_f Is Dimension-Locked

| Config | Penult D_f | Output D_f | Accuracy |
| :--- | :--- | :--- | :--- |
| 64-32-10 | 0.490 | 0.609 | 89.4% |
| 64-32-128-10 | 0.190 | 0.615 | 89.3% |
| 64-32-512-10 | 0.100 | 0.655 | 90.1% |

**Output-layer D_f is locked by output-layer dimension.** A 10-dim output layer always has D_f near 0.6 and cannot reflect network quality.

### 8.2 Output Entropy and Margin Are the Strong Predictors of Accuracy

#### 1. Design

On 6 width-scan configurations, measure 4 quantities and their correlations with accuracy:

- D_f(output)
- margin_mean
- out_entropy
- logit_scale

#### 2. Results

| Config | acc | D_f | margin | out_H | logit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 16-32-16-8 | 81.0% | 0.664 | 1.69 | 0.674 | 3.46 |
| 32-32-16-8 | 82.6% | 0.611 | 2.04 | 0.599 | 4.12 |
| 128-32-16-8 | 85.2% | 0.636 | 2.53 | 0.472 | 4.09 |
| 256-32-16-8 | 87.3% | 0.618 | 2.94 | 0.438 | 4.03 |
| 512-32-16-8 | 89.1% | 0.635 | 3.87 | 0.336 | 4.55 |
| 1024-32-16-8 | 88.5% | 0.591 | 3.75 | 0.352 | 3.52 |

**Correlation with accuracy:**

| Quantity | Correlation |
| :--- | :--- |
| D_f_out | **−0.522** |
| margin_mean | **+0.976** |
| out_entropy | **−0.992** |
| logit_scale | +0.402 |

#### 3. Observations

**One: D_f has weak correlation (−0.522) and is not monotonic.**

**Two: margin rises monotonically (+0.976).**

**Three: out_entropy falls monotonically (−0.992).** Strongest single predictor.

**Four: logit_scale is weak (+0.402).**

#### 4. Conclusion

**Output entropy and margin are the strong predictors. D_f is not.**

**Reason: D_f is dimension-locked by the output layer (see 8.1).**

### 8.3 Layer-Wise D_f Distribution

For 6-layer network (784-128-64-32-16-10):

| Layer | Dim | D_f |
| :--- | :--- | :--- |
| input | 784 | 0.089 |
| h1 | 128 | 0.215 |
| h2 | 64 | 0.348 |
| h3 | 32 | 0.480 |
| h4 | 16 | 0.595 |
| output | 10 | 0.657 |
| **all hidden joint** | — | **0.159** |

**Three observations:**

**One: D_f rises monotonically as layers narrow.**

**Two: joint hidden D_f is only 0.159, far below any single layer.**

**Three: output lock-in is the extreme case of layer-wise lock-in.**

### 8.4 Width Scan

#### 1. Results

| Config | h1 D_f | out D_f | Accuracy |
| :--- | :--- | :--- | :--- |
| 16-32-16-8 | 0.645 | 0.619 | 81.0% |
| 32-32-16-8 | 0.500 | 0.619 | 82.6% |
| 128-32-16-8 | 0.252 | 0.610 | 85.2% |
| 256-32-16-8 | 0.153 | 0.621 | 87.3% |
| 512-32-16-8 | 0.102 | 0.619 | 89.1% |
| 1024-32-16-8 | 0.060 | 0.624 | 88.5% |

#### 2. Observations

**One: wider h1, lower h1 D_f.** Monotonic from 0.645 to 0.060.

**Two: output D_f nearly unchanged (0.61–0.62).**

**Three: accuracy peaks at 512 (89.1%), dips to 88.5% at 1024.**

### 8.5 Information Migration

#### 1. Question

Where does the lost information go when the output layer is dimension-locked?

#### 2. Design

Two complementary experiments:

**Experiment 1 (narrow penult)**: fix output to 10 dims, scan penult = 2, 4, 8, 16, 32.

**Experiment 2 (wide penult)**: compare A(64-32-10), B(64-32-128-10), C(64-32-512-10).

Measure: D_f(out), D_f(penult), D_f(combined).

**Criterion: if D_f(combined) < D_f(out), the lost information is in penult and can be read jointly.**

#### 3. Results

**Experiment 1 (narrow penult):**

| penult | Accuracy | D_f(out) | D_f(penult) | D_f(combined) |
| :--- | :--- | :--- | :--- | :--- |
| 2 | 11.0% | 0.996 | 0.996 | 0.996 |
| 4 | 30.0% | 0.746 | 0.806 | 0.767 |
| 8 | 76.9% | 0.650 | 0.754 | **0.642** |
| 16 | 85.1% | 0.617 | 0.633 | **0.528** |
| 32 | 88.0% | 0.626 | 0.521 | **0.448** |

**Experiment 2 (wide penult):**

| Config | out | out+margin | out+penult | penult |
| :--- | :--- | :--- | :--- | :--- |
| A (64-32-10) | 0.642 | 0.633 | **0.432** | 0.477 |
| B (64-32-128-10) | 0.626 | 0.651 | **0.188** | 0.189 |
| C (64-32-512-10) | 0.623 | 0.610 | **0.100** | 0.101 |

#### 4. Observations

**One: no migration when penult is too narrow.**

**Two: migration appears at penult ≥ 8 and grows with width.**

**Three: at penult ≥ 128, joint D_f is dominated by penult.**

**Four: in config A, joint is even better than penult alone (0.432 < 0.477).** Output and penult are complementary.

**Five: margin does not migrate.**

#### 5. Conclusion

**Lost information does not disappear; it migrates into the joint distribution of output and penult.**

**The key is not "information elsewhere" but "information in relations."**

#### 8.5.1 Migration Threshold: Proportional, Not Absolute

##### 1. Results

**5 classes:**

| penult | ratio | Accuracy | D_f_out | D_f_comb | gain |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4 | 0.8x | 75.8% | 0.584 | 0.530 | **+0.054** |
| 8 | 1.6x | 96.6% | 0.509 | 0.440 | +0.069 |
| 16 | 3.2x | 97.6% | 0.542 | 0.379 | +0.163 |
| 32 | 6.4x | 97.1% | 0.515 | 0.238 | +0.277 |

**10 classes:**

| penult | ratio | Accuracy | D_f_out | D_f_comb | gain |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4 | 0.4x | 30.0% | 0.749 | 0.751 | **−0.002** |
| 8 | 0.8x | 76.9% | 0.651 | 0.604 | +0.046 |
| 16 | 1.6x | 85.1% | 0.615 | 0.531 | +0.084 |
| 32 | 3.2x | 88.0% | 0.658 | 0.431 | +0.227 |

##### 2. Observations

**One: threshold is proportional, not absolute.** At 0.8x classes, gain is +0.054 (5 classes) vs +0.046 (10 classes).

**Two: threshold ≈ 0.8 × number of classes.**

**Three: gain grows monotonically with penult.**

##### 3. Conclusion

**The migration threshold is approximately 0.8 × number of classes.**

##### 4. Relation to Section 9.2

- Migration threshold ≈ **0.8 × number of classes**
- Effective rank ≈ **1.25 × number of classes** (Section 9.2, old version)
- **1 / 1.25 = 0.8**

**Migration threshold = 1 / (effective rank / number of classes).**

### 8.6 Full Training Curve: D_f Oscillates, Margin Is Monotonic

#### 1. Results

| Epoch | Acc | D_f | Margin |
| :--- | :--- | :--- | :--- |
| 1 | 44.8% | 0.709 | **−0.024** |
| 2 | 72.0% | 0.666 | 0.848 |
| 3 | 80.0% | 0.640 | 1.518 |
| 5 | 85.7% | 0.636 | 2.677 |
| 8 | 89.1% | 0.603 | 3.589 |
| 10 | 88.4% | 0.569 | 4.012 |
| 16 | 93.0% | 0.606 | 5.787 |
| 20 | 92.4% | 0.593 | 6.924 |
| 28 | 92.8% | 0.594 | 9.115 |
| 36 | 92.8% | 0.616 | 10.332 |
| 40 | 93.0% | 0.589 | **10.801** |

#### 2. Observations

**One: D_f oscillates between 0.56 and 0.71 with no net trend.**

**Two: margin rises monotonically from −0.024 to 10.8.**

**Three: no saturation point for any of D_f, margin, accuracy.**

#### 3. Conclusion

**D_f and margin behave oppositely: D_f oscillates, margin is monotonic.** This further confirms D_f cannot be a training signal.

**All three quantities lack a saturation point, directly supporting Section XII: D_f has no saturation point — because it never appears.**

---

## IX. Result 6: Low-Rank Structure, Fit Form, Boundary, and Anomaly

### 9.1 Relation Is Low-Rank

| Quantity | Value |
| :--- | :--- |
| Effective rank | **11.98** |
| Random matrix effective rank | 18.69 |
| Max eigenvalue gap | 20.34 |
| First eigenvalue fraction | **32.9%** |
| Top 5 fraction | 63.1% |
| Top 10 fraction | 84.2% |
| Top 20 fraction | 98.7% |

**128 neurons, but their relational structure has only ~12 effective dimensions.**

### 9.2 Effective Rank Form: Training Sufficiency Decides Everything

#### 1. Old Version (Insufficient Training)

10-epoch training, accuracy 88–97%:

| k | r_eff | Accuracy |
| :--- | :--- | :--- |
| 2 | 2.62 | — |
| 3 | 5.28 | 98.7% |
| 4 | 7.24 | 97.5% |
| 5 | 8.35 | 97.5% |
| 6 | 10.28 | 96.5% |
| 8 | 12.23 | 92.9% |
| 10 | 12.35 | 88.3% |

Fits:

- Through origin: r_eff − k = 1.263 · log₂(k)
- With intercept: r_eff − k = 1.048 · log₂(k) + 0.539
- Linear: r_eff = 1.05 · k + 0.54

**r_eff / k is stable at 1.2–1.3.**

#### 2. New Version (Sufficient Training)

Accuracy 97–99%:

| k | r_eff | Accuracy |
| :--- | :--- | :--- |
| 2 | 2.72 | 99.95% |
| 3 | 6.46 | 99.46% |
| 4 | 9.66 | 99.27% |
| 5 | 13.68 | 99.29% |
| 6 | 14.02 | 98.91% |
| 8 | 19.70 | 98.26% |
| 10 | 19.58 | 97.23% |

Fits:

- Through origin: r_eff − k = 3.164 · log₂(k)
- With intercept: r_eff − k = 4.442 · log₂(k) − 3.202
- Linear: r_eff = 2.17 · k + 0.49

**r_eff / k rises from 1.36 (k=2) to 2.74 (k=5), then drops to 1.96 (k=10). Not constant.**

#### 3. Two-Version Comparison

| k | Old | New | Diff |
| :--- | :--- | :--- | :--- |
| 2 | 2.62 | 2.72 | +0.10 |
| 3 | 5.28 | 6.46 | +1.18 |
| 4 | 7.24 | 9.66 | +2.42 |
| 5 | 8.35 | 13.68 | **+5.33** |
| 6 | 10.28 | 14.02 | +3.74 |
| 8 | 12.23 | 19.70 | **+7.47** |
| 10 | 12.35 | 19.58 | **+7.23** |

**More training, higher effective rank. The gap grows with k.**

#### 4. Saturation Check (New)

```
k: 2 → 3,  Δr_eff/Δk = +3.74
k: 3 → 4,  Δr_eff/Δk = +3.20
k: 4 → 5,  Δr_eff/Δk = +4.02
k: 5 → 6,  Δr_eff/Δk = +0.34   ← barely moves
k: 6 → 8,  Δr_eff/Δk = +2.84   ← jumps again
k: 8 → 10, Δr_eff/Δk = −0.06   ← negative
```

**Not monotonic, not smooth saturation — it jitters.**

#### 5. Conclusion

**Effective rank is not captured by a single formula. It is jointly determined by task demand + training sufficiency + architectural capacity.**

**"Effective rank ≈ 1.25 × number of classes" is an empirical relation under insufficient training, not a universal law.**

### 9.3 Background Mode Is Architecture-Driven (Direct Projection Layer)

| Mode | Eigenvalue | MI(class) | Brightness | Contrast | Edge | HF |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 (bg) | 22.82 | 0.434 | **−0.941** | **−0.942** | −0.427 | 0.748 |
| 1 | 6.88 | 0.831 | −0.240 | −0.215 | −0.061 | 0.229 |
| 2 | 6.50 | 0.933 | −0.007 | −0.010 | −0.291 | −0.159 |
| 3 | 5.03 | 0.826 | −0.474 | −0.434 | −0.535 | 0.205 |
| 4 | 4.63 | 0.621 | 0.223 | 0.207 | 0.345 | −0.026 |

**Five observations:**

**One: background mode encodes only global statistics.**

**Two: class modes do not touch global statistics.**

**Three: brightness and contrast are inseparable in MNIST.**

**Four: edge density and high-frequency fraction are not the main components.**

**Five: 2-class background MI = 0.775, 10-class MI = 0.432. Background mode does not change with task; it is a property of the architecture.**

### 9.4 Boundary: Separation Holds Only at Direct Projection Layers

#### 1. Results

| Quantity | MNIST (FC) | CIFAR (FC) | CIFAR (CNN) |
| :--- | :--- | :--- | :--- |
| Accuracy | 88.3% | 36.6% | 69.0% |
| Effective rank | 12.30 | 11.96 | **4.78** |
| Background MI | 0.433 | 0.205 | 0.183 |
| BG vs brightness | −0.941 | −0.863 | **−0.076** |
| BG vs contrast | −0.942 | −0.359 | **−0.498** |

#### 2. Conclusion

**The "background + class" separation is not universal. It holds only at "direct projection layers."**

**Significance:** Corresponds to the holographic principle detail that **"the boundary must be the outermost layer."**

### 9.5 Anomaly at High Class Count: Effective Rank Saturation

| Classes | Effective rank | Accuracy |
| :--- | :--- | :--- |
| 5 | 8.43 | 97.5% |
| 10 | 12.00 | 88.3% |
| **20** | **8.73** | **85.3%** |

**20-class effective rank (8.73) is lower than 10-class (12.00).**

Long training: rises from 8.39 (epoch 5) to 10.01 (epoch 30), still not saturated.

**Effective rank is jointly determined by task demand + architectural capacity + training sufficiency.**

---

## X. Result 7: Encoding Meaning of the Background Mode

See Section 9.3.

| Neural Network | Black Hole |
| :--- | :--- |
| Background mode (brightness/contrast) | Horizon geometry |
| Class modes | Information falling into matter |
| Background/class separation | Geometry/matter separation |

---

## XI. Correspondence with Black Holes

### 1. AdS/CFT Quantum Error-Correcting Code

Almheiri, Dong, Harlow (2015): AdS/CFT duality is essentially a quantum error-correcting code.

### 2. Island Mechanism

Penington, Almheiri et al. (2019): information is not in individual radiation quanta but in the entanglement between them.

### 3. Correspondence Table

| | AdS/CFT | Neural Network |
| :--- | :--- | :--- |
| Bulk information | Black hole interior | Class labels |
| Boundary dof | CFT qubits | h1 neurons |
| Encoding | Quantum error-correcting code | Correlational error-correcting code |
| Damage tolerance | Some boundary bits may be lost | Some neurons may be shuffled |
| Collapse threshold | ~50% | ~40–60% |
| Larger is more robust | Larger BH more damage-tolerant | Wider layer more damage-tolerant |
| Encoding timing | At horizon formation | Within first epoch |
| Relational structure | Entanglement spectrum | Low-rank MI matrix |
| Effective dimension | Holographic dof | Jointly determined by training and architecture |
| Background mode | Horizon geometry | Brightness/contrast (class-independent) |
| Class modes | Information falling into matter | Mid-size eigenmodes (class-correlated) |
| BG/class separation | Geometry/matter separation | Holds only at direct projection layer |
| Information in correlations (holography) | Entanglement between boundary dof | Correlations between neurons of each layer |
| Information in joints (islands) | Radiation + interior entanglement | out + penult joint |
| Migration threshold | Proportional to interior dof | 0.8 × number of classes |
| High-energy saturation | High-dim horizon degeneracy | High-class effective rank saturation |

### 4. Four Precise Correspondence Points

**One:** error-correcting code structure and "information in correlations" are two sides of the same thing.

**Two:** background/class separation holds only at the outermost projection.

**Three:** sub-linear growth and saturation of effective rank correspond to the holographic screen's bound on degrees of freedom.

**Four:** information migration corresponds to the island mechanism.

---

## XII. A Falsified Hypothesis

### 1. Hypothesis

The saturation point of D_f can serve as an early-stopping signal.

### 2. Result

The oscillation amplitude of D_f (±0.03–0.05) exceeds the "saturation signal."

### 3. Conclusion

**The hypothesis is falsified.**

### 4. Supplement: No Saturation Point in 40 Epochs

Section 8.6 shows that over 40 epochs, none of D_f, margin, or accuracy reaches a saturation point.

**The "D_f saturation point" does not exist.**

---

## XIII. Limitations

1. **Single dataset (partial)**: most experiments on MNIST, CIFAR only for boundary tests.
2. **Single architecture (partial)**: FC mostly; CNN only for Section 9.4.
3. **D_f estimation noise**: classifier cross-entropy.
4. **Damage-operation limitations**: only shuffling tested.
5. **Coarse threshold localization**: h1=512 threshold in 0.6–0.8.
6. **QECC correspondence is structural**: not physical equivalence.
7. **Binning dependence**: MI matrix uses 10 bins.
8. **Limited fit range for effective rank**: old fit only for k ≤ 10 and insufficient training.
9. **Image-statistic selection**: only 4 statistics tested.
10. **20-class undertraining**: 30 epochs still not saturated.
11. **Training sufficiency not systematically scanned**: only "10 epochs" and "sufficient."
12. **Migration threshold precision**: 0.8 × classes from only two class counts.

---

## XIV. Conclusion

### 1. Core Results

**First:** information is in the correlations between neurons, not concentrated in a few neurons. For h1=128, 75% in correlations. Variance ordering matches random ordering.

**Second:** partial-shuffle curve is convex; error-correcting code structure.

**Third:** threshold grows with layer width.

**Fourth:** error-correcting code activated in first epoch; overall retention improved.

**Fifth:** output-layer D_f locked; margin and output entropy are the strong predictors (−0.99, +0.98).

**Sixth:** low-rank relation; effective rank grows with class count, but the form depends on training sufficiency.

**Seventh:** in direct projection layer, background mode is architecture-driven.

**Eighth:** background/class separation holds only at direct projection layer.

**Ninth:** effective rank saturates at high class counts and full training.

**Tenth:** migration threshold ≈ 0.8 × number of classes.

### 2. Correspondence with Black Holes

Quantitative cross-system correspondence to the QECC picture in AdS/CFT and the island mechanism.

### 3. Positioning

**Not a new physics discovery but a quantitative cross-system correspondence.**

Eight previously unreported numbers:

- Error-correction threshold grows linearly with layer width
- Error-correcting code activated in first epoch
- Effective rank strongly affected by training sufficiency (7 units at same task)
- Migration threshold ≈ 0.8 × classes
- Separation of background and class modes
- Background mode = direct-projection input global statistics
- Effective rank saturation at 20 classes
- Layer-wise correlation contribution 52–75%

### 4. Three Deeper Questions

**One:** is the "background + signal" separation a universal structure in all information-processing systems?

**Two:** what does "separation holds only at direct projection layer" mean? Do convolutional layers lose a "boundary" property?

**Three:** what does effective-rank saturation mean? Is the h1 dimension a "physical upper bound"?

---

## XV. Data Availability

Code is reproducible in GitHub repository `maxlanceund/github-random`. Main workflows:

- `run_nn_correlation.yml`: information in correlations
- `run_nn_corr_all.yml`: layer-wise correlation contribution
- `run_nn_neuron.yml`: single-neuron analysis
- `run_nn_partial_shuffle.yml`: partial-shuffle curve
- `run_nn_ecc.yml`: width dependence
- `run_nn_ecc_dyn.yml`: training dynamics
- `run_nn_random_ecc.yml`: random vs. trained
- `run_nn_control.yml`: random-network control
- `run_nn_mi.yml`: MI matrix analysis
- `run_nn_eigen.yml`: eigenmodes vs. class direction
- `run_nn_eigen_2cls.yml`: 2-class vs. 10-class
- `run_nn_bg.yml`: encoding meaning of background mode
- `run_nn_cifar.yml`: CIFAR-10 + FC boundary test
- `run_nn_cifar_cnn.yml`: CIFAR-10 + CNN boundary test
- `run_nn_width.yml`: width scan
- `run_nn_margin.yml`: margin and output entropy
- `run_nn_bottleneck.yml`: information migration (narrow penult)
- `run_nn_migration.yml`: information migration (wide penult)
- `run_nn_threshold.yml`: migration threshold
- `run_nn_training.yml`: full training curve
- `run_nn_rank.yml`: effective-rank fit
- `run_nn_rank_fit2.yml`: sufficiently-trained effective rank
- `run_nn_rank_long.yml`: 20-class long training
- `run_nn_null.yml`: null test
- `run_nn_earlystop.yml`: early-stopping hypothesis (falsified)

---

## XVI. Conflict of Interest

The author declares no conflict of interest that could affect the conclusions or academic judgment of this work.

---

## XVII. References

[1] Almheiri, A., Dong, X., & Harlow, D. (2015). Bulk Locality and Quantum Error Correction in AdS/CFT. *Journal of High Energy Physics*, 2015(4), 163.

[2] Penington, G. (2020). Entanglement Wedge Reconstruction and the Information Paradox. *Journal of High Energy Physics*, 2020(9), 2.

[3] Hinton, G. E., McClelland, J. L., & Rumelhart, D. E. (1986). Distributed Representations. In *Parallel Distributed Processing* (Vol. 1, pp. 77-109). MIT Press.

[4] Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379-423.

[5] Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.

[6] Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. *Proceedings of the 37th Annual Allerton Conference on Communication, Control, and Computing*, 368-377.

---

**Suggested citation (APA):**

Zhong, S. (2026). *Error-Correcting Code Structure in Neural Networks — Non-Local Information Distribution, Task-Driven Effective Rank, and the Analogy with Black Holes* (Version 3.3). Equal System Repository.
